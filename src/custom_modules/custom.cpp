/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#define _USE_MATH_DEFINES
#include <cmath>
#include <sstream>
#include "./custom.h"
#include "../BioFVM/BioFVM.h"  

using namespace BioFVM;
using namespace PhysiCell;
// declare cell definitions here 

// std::string ecm_file;
std::vector<bool> nodes;

void create_cell_types( void )
{
		// set the random seed 
	SeedRandom( parameters.ints("random_seed") );  
	
	/* 
	   Put any modifications to default cell definition here if you 
	   want to have "inherited" by other cell types. 
	   
	   This is a good place to set default functions. 
	*/ 
	
	cell_defaults.functions.volume_update_function = standard_volume_update_function;
	//cell_defaults.functions.update_velocity = standard_update_cell_velocity;

	cell_defaults.functions.update_migration_bias = NULL;  
	
	cell_defaults.functions.add_cell_basement_membrane_interactions = NULL; 
	cell_defaults.functions.calculate_distance_to_membrane = NULL; 
	cell_defaults.functions.contact_function = standard_elastic_contact_function;

			/*
	   This parses the cell definitions in the XML config file. 
	*/
	
	initialize_cell_definitions_from_pugixml(); 

	/* 
	   Put any modifications to individual cell definitions here. 
	   
	   This is a good place to set custom functions. 
	*/ 


	cell_defaults.functions.update_phenotype = tumor_cell_phenotype_with_signaling; 


		/*
	   This builds the map of cell definitions and summarizes the setup. 
	*/
		
	


	cell_defaults.functions.cycle_model.phase_link(0,1).arrest_function = wait_for_cell_growth;
	cell_defaults.functions.cycle_model.phase_link(1,2).arrest_function = wait_for_nucleus_growth;

	int TGFbeta_index = microenvironment.find_density_index("TGFbeta");
	cell_defaults.phenotype.secretion.uptake_rates[TGFbeta_index] = PhysiCell::parameters.doubles("TGFbeta_degradation");
	int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "apoptosis" );
	cell_defaults.phenotype.death.rates[apoptosis_model_index] = 0.0;
	cell_defaults.phenotype.death.models[apoptosis_model_index]->phase_link(0,1).arrest_function = waiting_to_remove; 
	int oxygen_index = microenvironment.find_density_index("oxygen");
	cell_defaults.phenotype.secretion.uptake_rates[oxygen_index] = 10.0;

	
	// add custom data here, if any

	//Setting the custom_create_cell pointer to our create_custom_cell
	// cell_defaults.functions.custom_cell_rule = Custom_cell::check_passive;
	cell_defaults.functions.update_velocity = custom_update_velocity;
	cell_defaults.functions.custom_cell_rule = ecm_cell_function;
	// cell_defaults.functions.add_cell_basement_membrane_interactions = Custom_cell::add_cell_basement_membrane_interactions;	
	// cell_defaults.functions.calculate_distance_to_membrane = Custom_cell::distance_to_membrane;

	
	build_cell_definitions_maps(); 
	display_cell_definitions( std::cout ); 
	return; 
}

void setup_microenvironment( void )
{
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == true )
	 {
	// 	std::cout << "Warning: overriding XML config option and setting to 3D!" << std::endl; 
	// 	default_microenvironment_options.simulate_2D = false; 
		cell_defaults.functions.set_orientation = up_orientation; 
		cell_defaults.phenotype.geometry.polarity = 1.0;
	 }	

	// initialize BioFVM 
	initialize_microenvironment(); 	
	
	return; 
}




void setup_tissue( void )
{
	//std::vector<init_record> cells = read_init_file(parameters.strings("init_cells_filename"), ';', true);
	double cell_radius = cell_defaults.phenotype.geometry.radius; 
	double cell_spacing = 0.95 * 2.0 * cell_radius; 
	
	double tumor_radius = parameters.doubles("config_radius");

	std::vector<std::vector<double>> positions;

	if (default_microenvironment_options.simulate_2D == true){
		positions = create_cell_disc_positions(cell_radius,tumor_radius);
		std::cout << "ENABLED 2D SIMULATION"; 
	}
	else
		positions = create_cell_sphere_positions(cell_radius,tumor_radius);

	Cell* pCell = NULL;

	for (int i = 0; i < positions.size(); i++)
	{

		pCell = create_cell(get_cell_definition("default")); 
		pCell->assign_position( positions[i] );

		// double volume = sphere_volume_from_radius(cell_radius);
		// pCell->set_total_volume(volume);
		// pCell->phenotype.volume.target_solid_nuclear = cell_defaults.phenotype.volume.target_solid_nuclear;
		// pCell->phenotype.volume.target_solid_cytoplasmic = cell_defaults.phenotype.volume.target_solid_cytoplasmic;
		// pCell->phenotype.volume.rupture_volume = cell_defaults.phenotype.volume.rupture_volume; 
	
		//pC->phenotype.cycle.data.current_phase_index = phase+1;
		//pC->phenotype.cycle.data.elapsed_time_in_phase = elapsed_time;
		//if ((phase+1) == 1)
			//pC->phenotype.cycle.pCycle_Model->phases[1].entry_function(pC, pC->phenotype, 0);

		color_node(pCell);
		//std::cout << pC->phenotype.intracellular->get_boolean_node_value("Cell_growth");
		//pC->phenotype.intracellular->print_current_nodes();
		//std::cout << std::endl;
	}
	std::cout << "tissue created" << std::endl;

	return; 
}

void tumor_cell_phenotype_with_signaling( Cell* pCell, Phenotype& phenotype, double dt )
{

	if( phenotype.death.dead == true )
	{
		pCell->functions.update_phenotype = NULL;
		return;
	}


	if (pCell->phenotype.intracellular->need_update())
	{
		//  std::cout << "setting input nodes" << "\n";
		//pCell->phenotype.intracellular->print_current_nodes();
		set_input_nodes(pCell);
		
		pCell->phenotype.intracellular->update();

		from_nodes_to_cell(pCell, phenotype, dt);
		//std::cout << std::endl << pCell->phenotype.intracellular->get_boolean_variable_value( "ECM_adh" ) << "        " << pCell->custom_data["integrin"];
		color_node(pCell);
		
	}

	
}

void set_input_nodes(Cell* pCell) 
{	

	pCell->phenotype.intracellular->set_boolean_variable_value("optoSRC", sense_light(pCell));
	
	pCell->phenotype.intracellular->set_boolean_variable_value("Oxy", !necrotic_oxygen(pCell));
	
	
	// 	nodes[ind] = ( !pCell->necrotic_oxygen() );

	//enough_to_node( pCell, "TGFbR", "tgfb" );

	
	pCell->phenotype.intracellular->set_boolean_variable_value("Neigh", has_neighbor(pCell, 0));	
	
	
	
	//pCell->phenotype.intracellular->set_boolean_variable_value("Nei2", has_neighbor(pCell, 1));
	
	
	// If has enough contact with ecm or not
	
	pCell->phenotype.intracellular->set_boolean_variable_value("ECM", touch_ECM(pCell));
	
	// If has enough contact with TGFbeta or not
	
	pCell->phenotype.intracellular->set_boolean_variable_value("TGFbeta", touch_TGFbeta(pCell));

	// If nucleus is deformed, probability of damage
	// Change to increase proba with deformation ? + put as parameter
	
	/*if ( pCell->phenotype.intracellular->has_variable( "DNAdamage" ) )
		pCell->phenotype.intracellular->set_boolean_variable_value("DNAdamage", 
			( pCell->custom_data["nucleus_deform"] > 0.5 ) ? (2*PhysiCell::UniformRandom() < pCell->custom_data["nucleus_deform"]) : 0
		);*/

	if ( pCell->phenotype.intracellular->has_variable( "DNAdamage" ) ){

		double pressure = pCell->state.simple_pressure;
		double pressure_threshold = 8.0;
		pCell->phenotype.intracellular->set_boolean_variable_value("DNAdamage", 
			( pressure > pressure_threshold ) ? (8 * PhysiCell::UniformRandom() < pressure) : 0
		);
	}
	/// example
	
}

void from_nodes_to_cell(Cell* pCell, Phenotype& phenotype, double dt)
{
	if (pCell->phenotype.intracellular->get_boolean_variable_value( "Apoptosis" ) )
	{
		int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "apoptosis" );
		pCell->start_death(apoptosis_model_index);
		std::cout << "died for apoptosis!"<< std::endl;
		return;
	}
	/*
	if ( pCell->phenotype.intracellular->get_boolean_variable_value( "Hypoxia" ) )
	{
		int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "necrosis" );
		pCell->start_death(necrosis_model_index);
		std::cout << "died for necrosis!"<< std::endl;
		return;
	}
*/
	if ( pCell->phenotype.intracellular->has_variable("Migration"))
	{
		set_oxygen_motility(pCell, pCell->phenotype.intracellular->get_boolean_variable_value("Migration"));
		evolve_motility_coef(pCell, pCell->phenotype.intracellular->get_boolean_variable_value( "Migration" ), dt );
	}
		/*		
	if ( pCell->phenotype.intracellular->has_node( "Single" ) 
		&& pCell->phenotype.intracellular->get_boolean_node_value( "Single" ) 
	)
	{
		pCell->padhesion = 0;
	}
	*/
	/*
	 if ( pCell->phenotype.intracellular->get_boolean_variable_value("MCM2") ){
	 	do_proliferation( pCell, phenotype, dt );
	 }
*/
	/*if ( pCell->phenotype.intracellular->has_node( "Polarization" ) )
		pCell->evolve_polarity_coef( 
			pCell->phenotype.intracellular->get_boolean_node_value( "Polarization" ), dt 
		);
	*/

	if ( pCell->phenotype.intracellular->has_variable( "EMT" )){
		evolve_cellcell_coef( pCell, !(pCell->phenotype.intracellular->get_boolean_variable_value( "EMT" )), dt);
		if (pCell->phenotype.intracellular->get_boolean_variable_value( "EMT" ))
			custom_detach_cells(pCell);
		else
			custom_cell_attach(pCell);
		}

	if ( pCell->phenotype.intracellular->has_variable( "ECM_adh" )){

		//std::cout << std::endl << pCell->phenotype.intracellular->get_boolean_variable_value( "ECM_adh" ) << "        " << pCell->custom_data["integrin"];

		evolve_integrin_coef( pCell,
			pCell->phenotype.intracellular->get_boolean_variable_value( "ECM_adh" ), dt 
		);
		}

	if ( pCell->phenotype.intracellular->has_variable("ECM_degrad") ){
	 	set_mmp(pCell, pCell->phenotype.intracellular->get_boolean_variable_value("ECM_degrad") );}


	freezing(pCell, 0 );
	/*
	if ( pCell->phenotype.intracellular->get_boolean_variable_value( "CellCycleArrest" ) ){
		freezing(pCell, 1);
	}
	*/
	/*
	if ( pCell->phenotype.intracellular->has_variable( "Cell_freeze" ) ){
		freezer(pCell, 3 * pCell->phenotype.intracellular->get_boolean_variable_value( "Cell_freeze" ));
	}
	*/
	//pCell->phenotype.intracellular->print_current_nodes();
}

/* Update the value of freezing of the cell with bitwise operation
* Do a bitwise-or comparison on freezed and input parameter:
* if freezed = 0, it will be the value of the parameter frozen
* if freezed = 1, it will be either 1 (frozen = 0) or 3 (frozen = 3) */
void freezer( Cell* pC, int frozen )
{
	int freezed = pC->custom_data["freezed"];
    pC->custom_data["freezed"] = freezed | frozen;
}

bool waiting_to_remove(Cell* cell, Phenotype& phenotype, double dt) {
	if (cell->phenotype.cycle.data.elapsed_time_in_phase >= (8.6 * 60.0))
		return false;
	
	if (cell->phenotype.volume.total < PhysiCell_constants::cell_removal_threshold_volume) 
		return false;

	return true;
}

bool wait_for_nucleus_growth (Cell* cell, Phenotype& phenotype, double dt) {
	return (relative_diff( 
		cell->phenotype.volume.total, 
		pow(PhysiCell::parameters.doubles("cell_radius"), 3.0) * 3.14159 * (4.0/3.0) * 2.0 
	) > UniformRandom() * 0.1);
}

/* Calculate adhesion coefficient with other cell */
double adhesion(Cell* pCell, Cell* other_cell )
{	
	double adh = 0;	
	if ( pCell->type == other_cell->type )
		adh = std::min( get_homotypic_strength(pCell->custom_data["padhesion"]), get_homotypic_strength(other_cell->custom_data["padhesion"]) );
	else
		adh = std::min( get_heterotypic_strength(pCell->custom_data["padhesion"]), get_heterotypic_strength(other_cell->custom_data["padhesion"]) );

	return adh;
}

void custom_cell_attach(Cell* pCell){

	// check the neighbors of current cells, if there is a high level of integrins, it triggers the attachment

	std::vector<Cell*> neigh = pCell->nearby_interacting_cells(); 

	double junction = pCell->custom_data["padhesion"];

	if (neigh.size() == 0)
		return ;

	for (int i = 0; i != neigh.size(); i++){

		double otherJunction = neigh[i]->custom_data["padhesion"];

		//should I also check the distance between the cells?

		if (junction + otherJunction > PhysiCell::parameters.doubles("cell_junctions_attach_threshold"))
			attach_cells( neigh[i] , pCell ); 

	}

}

void custom_detach_cells(Cell* pCell){

	double junction = pCell->custom_data["padhesion"];

	for (auto cell_attached : pCell->state.attached_cells){

		double otherJunction = cell_attached->custom_data["padhesion"];

		if (junction + otherJunction < PhysiCell::parameters.doubles("cell_junctions_detach_threshold"))
			detach_cells( cell_attached , pCell );

	};

	if (junction == 0.0)
		pCell->remove_all_attached_cells();

}

double custom_repulsion_function(Cell* pCell, Cell* otherCell) 
{
	if (pCell->custom_data["passive"] == 0)
		return 0; // Sphere are not affected by repulsion
	else
		return sqrt( pCell->phenotype.mechanics.cell_cell_repulsion_strength * otherCell->phenotype.mechanics.cell_cell_repulsion_strength ); 
}	

double custom_adhesion_function(Cell* pCell, Cell* otherCell, double distance) 
{

	// hyp: junction strength is limited by weakest cell
	double adh;
	bool thisadh = pCell->custom_data["passive"];
	bool otadh = otherCell->custom_data["passive"];
	// first case, passive cell with active cell
	if ( thisadh == 0 && otadh == 1 )
	{
		pCell->custom_data["ecm_contact"] += distance;
		//adh = integrinStrength(otherCell);
	}
	else
	{
		// second case, active cell with passive cell
		if ( thisadh == 1 && otadh == 0 )
		{
			pCell->custom_data["ecm_contact"] += distance;
			//adh = integrinStrength(pCell);
		}
		else
		{
			// passive, passive
			if ( thisadh == 0 && otadh == 0 )
			{
				adh = 0;
			}
			// active, active
			else
			{
				double perc_distance = distance / pCell->phenotype.geometry.radius ;
				pCell->custom_data["cell_contact"] += perc_distance;
				//std::cout << pCell->custom_data["cell_contact"] << "\n";
				adh = adhesion(pCell, otherCell);
				pCell->custom_data["adh"] = adh;
			}
		}
	}
	return adh;
}

//function stolen by virus_macrophage sample to check neighbors
std::vector<Cell*> get_possible_neighbors( Cell* pCell )
{
	std::vector<Cell*> neighbors = {}; 

	// First check the neighbors in my current voxel
	std::vector<Cell*>::iterator neighbor;
	std::vector<Cell*>::iterator end =
		pCell->get_container()->agent_grid[pCell->get_current_mechanics_voxel_index()].end();
	for( neighbor = pCell->get_container()->agent_grid[pCell->get_current_mechanics_voxel_index()].begin(); neighbor != end; ++neighbor)
	{ neighbors.push_back( *neighbor ); }

	std::vector<int>::iterator neighbor_voxel_index;
	std::vector<int>::iterator neighbor_voxel_index_end = 
		pCell->get_container()->underlying_mesh.moore_connected_voxel_indices[pCell->get_current_mechanics_voxel_index()].end();

	for( neighbor_voxel_index = 
		pCell->get_container()->underlying_mesh.moore_connected_voxel_indices[pCell->get_current_mechanics_voxel_index()].begin();
		neighbor_voxel_index != neighbor_voxel_index_end; 
		++neighbor_voxel_index )
	{
		if(!is_neighbor_voxel(pCell, pCell->get_container()->underlying_mesh.voxels[pCell->get_current_mechanics_voxel_index()].center, pCell->get_container()->underlying_mesh.voxels[*neighbor_voxel_index].center, *neighbor_voxel_index))
			continue;
		end = pCell->get_container()->agent_grid[*neighbor_voxel_index].end();
		for(neighbor = pCell->get_container()->agent_grid[*neighbor_voxel_index].begin();neighbor != end; ++neighbor)
		{ neighbors.push_back( *neighbor ); }
	}

	//std::cout << neighbors.size() << "\n";
	
	return neighbors;

}

//custom function to set adhesion and repulsion ---> very useful(?) for implementation of ECM agents
void ecm_cell_function (Cell* pCell, Phenotype& phenotype, double dt){

	std::vector<Cell*> neighbors = get_possible_neighbors(pCell);

	if (neighbors.size() == 0){

		return ; // what happened if I don't have any neigh? should I set adhesion and repulsion to 0? I think so...
	};
	
	Cell* OtherCell = NULL;
	pCell->custom_data["cell_contact"] = 0;
	for( int n=0; n < neighbors.size() ; n++ )
	{
		OtherCell = neighbors[n]; 
		// check if it's not me in the vector
		if( OtherCell != pCell )
		{
			// calculate distance to the cell 
			std::vector<double> displacement = OtherCell->position;
			displacement -= pCell->position;
			double distance = norm( displacement ); 
			
			double max_distance = pCell->phenotype.geometry.radius + 
				OtherCell->phenotype.geometry.radius; 
			max_distance *=  1.1;  //parameters.doubles("max_interaction_factor"); 

			//std::cout << max_distance << " - " << distance << "\n";

			double interaction_distance = max_distance - distance;
			if (interaction_distance < 0){
				continue ;
			}
			
			// calculate adhesion using custom function
			pCell->phenotype.mechanics.cell_cell_adhesion_strength = custom_adhesion_function(pCell, OtherCell, interaction_distance);

			//std::cout << pCell->phenotype.mechanics.cell_cell_adhesion_strength << " \n " ; 


			// calculate repulsion with custom function

			pCell->phenotype.mechanics.cell_cell_repulsion_strength = custom_repulsion_function(pCell, OtherCell);

		}
	}

	//std::cout << pCell->custom_data["cell_contact"] << "\n";


}

/** \brief (De)-Activate ECM degradation by the cell */
void set_mmp(Cell* pCell, int activate )
{ 
	int ecm_index = pCell->get_microenvironment()->find_density_index("ecm");

	if (activate){
		pCell->phenotype.secretion.uptake_rates[ecm_index] = PhysiCell::parameters.doubles("ecm_degradation") * pCell->custom_data["integrin"];
	}
		
	else
		pCell->phenotype.secretion.uptake_rates[ecm_index] = 0;
	
}

void set_oxygen_motility(Cell* pC, bool active)
{	
	//phenotype.motility.is_motile = active;
		
	if (active){
		pC->phenotype.motility.chemotaxis_index = pC->get_microenvironment()->find_density_index( "oxygen");
		// bias direction is gradient for the indicated substrate 
		pC->phenotype.motility.migration_bias_direction = pC->nearest_gradient(pC->phenotype.motility.chemotaxis_index);
		pC->phenotype.motility.migration_bias = PhysiCell::parameters.doubles("migration_bias");
		pC->phenotype.motility.chemotaxis_direction = 1.0;
		pC->phenotype.motility.migration_speed = PhysiCell::parameters.doubles("migration_speed");
		pC->phenotype.motility.persistence_time = PhysiCell::parameters.doubles("persistence");
		// move up or down gradient based on this direction 
		pC->phenotype.motility.migration_bias_direction *= pC->phenotype.motility.chemotaxis_direction * get_motility_amplitude(pC->custom_data["pmotility"]); 
	}
	else{
		//restore to default
		pC->phenotype.motility.chemotaxis_index = cell_defaults.phenotype.motility.chemotaxis_index; 
		pC->phenotype.motility.migration_bias_direction = cell_defaults.phenotype.motility.migration_bias_direction;
		pC->phenotype.motility.migration_bias = cell_defaults.phenotype.motility.migration_bias;
		pC->phenotype.motility.chemotaxis_direction = cell_defaults.phenotype.motility.chemotaxis_direction;
		pC->phenotype.motility.migration_speed = cell_defaults.phenotype.motility.migration_speed;
		pC->phenotype.motility.persistence_time = cell_defaults.phenotype.motility.persistence_time;
	 	}
};

/* Calculate repulsion/adhesion between agent and ecm according to its local density */
void add_ecm_interaction(Cell* pC, int index_ecm, int index_voxel )
{
	// Check if there is ECM material in given voxel
	//double dens2 = get_microenvironment()->density_vector(index_voxel)[index_ecm];
	double dens = pC->get_microenvironment()->nearest_density_vector(index_voxel)[index_ecm];
	double ecmrad = sqrt(3.0) * pC->get_microenvironment()->mesh.dx / 2.0;
	// if voxel is "full", density is 1
	dens = std::min( dens, 1.0 ); 
	if ( dens > EPSILON )
	{
		// Distance between agent center and ECM voxel center
		pC->displacement = pC->position - pC->get_container()->underlying_mesh.voxels[index_voxel].center;
		double distance = norm(pC->displacement);
		// Make sure that the distance is not zero
		distance = std::max(distance, EPSILON);
		
		double dd = pC->phenotype.geometry.radius + ecmrad;  
		double dnuc = pC->phenotype.geometry.nuclear_radius + ecmrad;  

		double tmp_r = 0;
		// Cell overlap with ECM node, add a repulsion term
		if ( distance < dd )
		{
			// repulsion stronger if nucleii overlap, see Macklin et al. 2012, 2.3.1
			if ( distance < dnuc )
			{
				double M = 1.0;
				double c = 1.0 - dnuc/dd;
				c *= c;
				c -= M;
				tmp_r = c*distance/dnuc + M;
				pC->custom_data["nucleus_deform"] += (dnuc-distance);
			}
			else
			{
				tmp_r = ( 1 - distance / dd );
				tmp_r *= tmp_r;
			}
			tmp_r *= dens * PhysiCell::parameters.doubles("cell_ecm_repulsion");
		}

		// Cell adherence to ECM through integrins
		double max_interactive_distance = (PhysiCell::parameters.doubles("max_interaction_factor")*pC->phenotype.geometry.radius) + ecmrad;
		if ( distance < max_interactive_distance ) 
		{	
			double temp_a = 1 - distance/max_interactive_distance; 
			temp_a *= temp_a; 
			/* \todo change dens with a maximal density ratio ? */
			pC->custom_data["ecm_contact"] += dens * (max_interactive_distance-distance);
			// temp_a *= dens * ( static_cast<Cell*>(this) )->integrinStrength();

			double temp_integrins = get_integrin_strength( pC->custom_data["integrin"] );

			temp_a *= dens * temp_integrins;
			
			tmp_r -= temp_a;
		}
		
		/////////////////////////////////////////////////////////////////
		if(tmp_r==0)
			return;
		tmp_r/=distance;

		pC->velocity += tmp_r * pC->displacement;
	}
}

void add_TGFbeta_interaction(Cell* pC, int index_voxel){
	double ecmrad = sqrt(3.0) * pC->get_microenvironment()->mesh.dx / 2.0;
	int TGFbeta_index = BioFVM::microenvironment.find_density_index( "TGFbeta" );
	int ecm_index = BioFVM::microenvironment.find_density_index( "ecm" );
	double dens_tgfb = pC->get_microenvironment()->nearest_density_vector(index_voxel)[TGFbeta_index];
	double dens_ecm = pC->get_microenvironment()->nearest_density_vector(index_voxel)[ecm_index];
	dens_tgfb = std::min( dens_tgfb, 1.0 );
	dens_ecm = std::min( dens_ecm, 1.0 );
	double ratio = dens_ecm / dens_tgfb;
	
	if(ratio < PhysiCell::parameters.doubles("ECM_TGFbeta_ratio")){
	pC->custom_data["TGFbeta_contact"] = 0;
	//std::cout << "dens =" << dens << std::endl; 
		if ( dens_tgfb > EPSILON )
		{
			// Distance between agent center and ECM voxel center
			pC->displacement = pC->position - pC->get_container()->underlying_mesh.voxels[index_voxel].center;
			double distance = norm(pC->displacement);
			// Make sure that the distance is not zero
			distance = std::max(distance, EPSILON);

			double max_interactive_distance = (PhysiCell::parameters.doubles("max_interaction_factor")*pC->phenotype.geometry.radius) + ecmrad;
			if ( distance < max_interactive_distance ) 
			{	
				pC->custom_data["TGFbeta_contact"] += dens_tgfb * (max_interactive_distance-distance);
				//std::cout << "TGFbeta =" << pC->custom_data["TGFbeta_contact"] << std::endl; 
			}
		}
	}
}

void custom_update_velocity( Cell* pCell, Phenotype& phenotype, double dt)
{
	pCell->custom_data["ecm_contact"] = 0;
	pCell->custom_data["nucleus_deform"] = 0;
	
	if( pCell->functions.add_cell_basement_membrane_interactions )
	{
		pCell->functions.add_cell_basement_membrane_interactions(pCell, phenotype,dt);
	}
	
	pCell->state.simple_pressure = 0.0; 
	
	//First check the neighbors in my current voxel
	for( auto neighbor : pCell->get_container()->agent_grid[pCell->get_current_mechanics_voxel_index()] )
	{
		pCell->add_potentials( neighbor );
	}

	pCell->state.simple_pressure = 0.0; 
	pCell->state.neighbors.clear(); // new 1.8.0

	std::vector<Cell*>::iterator neighbor;
	std::vector<Cell*>::iterator end = pCell->get_container()->agent_grid[pCell->get_current_mechanics_voxel_index()].end();
	for(neighbor = pCell->get_container()->agent_grid[pCell->get_current_mechanics_voxel_index()].begin(); neighbor != end; ++neighbor)
	{
		pCell->add_potentials(*neighbor);
	}
	std::vector<int>::iterator neighbor_voxel_index;
	std::vector<int>::iterator neighbor_voxel_index_end = 
		pCell->get_container()->underlying_mesh.moore_connected_voxel_indices[pCell->get_current_mechanics_voxel_index()].end();

	for( neighbor_voxel_index = 
		pCell->get_container()->underlying_mesh.moore_connected_voxel_indices[pCell->get_current_mechanics_voxel_index()].begin();
		neighbor_voxel_index != neighbor_voxel_index_end; 
		++neighbor_voxel_index )
	{
		if(!is_neighbor_voxel(pCell, pCell->get_container()->underlying_mesh.voxels[pCell->get_current_mechanics_voxel_index()].center, pCell->get_container()->underlying_mesh.voxels[*neighbor_voxel_index].center, *neighbor_voxel_index))
			continue;
		end = pCell->get_container()->agent_grid[*neighbor_voxel_index].end();
		for(neighbor = pCell->get_container()->agent_grid[*neighbor_voxel_index].begin();neighbor != end; ++neighbor)
		{
			pCell->add_potentials(*neighbor);
		}
	}

	int ecm_index = BioFVM::microenvironment.find_density_index("ecm");
	if ( ecm_index >= 0 ){
		add_ecm_interaction( pCell, ecm_index, pCell->get_current_mechanics_voxel_index() );
		add_TGFbeta_interaction(pCell, pCell->get_current_mechanics_voxel_index());
	}
/*
	if (pCell->custom_data["freezed"] > 2){
		return ;
	}
*/
	
	pCell->update_motility_vector(dt);
	//std::cout << pCell->state.simple_pressure << " \n ";
	pCell->velocity += phenotype.motility.motility_vector;
	
	return; 
}


void set_substrate_density(int density_index, double max, double min, double radius)
{
	std::cout << "SETTING SUBSTRATE \n";
	// Inject given concentration on the extremities only

	std::cout << microenvironment.number_of_voxels() << "\n";
	#pragma omp parallel for
	for (int n = 0; n < microenvironment.number_of_voxels(); n++)
	{
		auto current_voxel = microenvironment.voxels(n);
		double t_norm = norm(current_voxel.center);

		if ((radius - t_norm) <= 0)
			microenvironment.density_vector(n)[density_index] = current_value(min, max, uniform_random());
	}
}

/* Return if cell has enough contact with other cells (compared to given threshold determined by the given level) */	
bool has_neighbor(Cell* pCell, int level)
{ 
	if ( level == 0 ){
		return contact_cell(pCell) > PhysiCell::parameters.doubles("contact_cell_cell_threshold"); 
		}
	else{
		//std::cout << contact_cell() << " - " << PhysiCell::parameters.doubles("contact_cell_cell_threshold") << std::endl;
		return contact_cell(pCell) > (2 * PhysiCell::parameters.doubles("contact_cell_cell_threshold")); 
	}
}

/* Return true if level of oxygen is lower than necrosis critical level */
bool necrotic_oxygen(Cell* pCell)
{	
	int oxygen_substrate_index = BioFVM::microenvironment.find_density_index( "oxygen" );
	double ox = (pCell->nearest_density_vector())[oxygen_substrate_index];
	//std::cout << ox << " " << (this->parameters.o2_necrosis_threshold) - ox << std::endl;
	if ( ox >= 0 )	
		return ( UniformRandom() * 5 < (pCell->parameters.o2_necrosis_threshold - ox) );
   return false;	
}

/* Go to proliferative if needed */
void do_proliferation( Cell* pCell, Phenotype& phenotype, double dt )
{
	// If cells is in G0 (quiescent) switch to pre-mitotic phase
	if ( pCell->phenotype.cycle.current_phase_index() == PhysiCell_constants::Ki67_negative )
		pCell->phenotype.cycle.advance_cycle(pCell, phenotype, dt);
}

double sphere_volume_from_radius(double rad)
{
	double PI4_3 = 4.0 / 3.0 * M_PI;
return PI4_3 * rad * rad * rad;
}

bool touch_ECM(Cell* pCell)
{ 
	return contact_ecm(pCell) > parameters.doubles("contact_cell_ECM_threshold"); 
}

bool touch_TGFbeta(Cell* pCell){

	return contact_TGFB(pCell) > parameters.doubles("contact_TGFB_threshold");
}

void enough_to_node( Cell* pCell, std::string nody, std::string field )
{
	if ( pCell->phenotype.intracellular->get_boolean_variable_value(nody) )
	{
		int felt = feel_enough(field, pCell);
		if ( felt != -1 )
			pCell->phenotype.intracellular->set_boolean_variable_value(nody, felt);
	}
}

void color_node(Cell* pCell){
	std::string node_name = parameters.strings("node_to_visualize");
	pCell->custom_data["node"] = pCell->phenotype.intracellular->get_boolean_variable_value(node_name);
}

std::vector<std::vector<double>> create_cell_sphere_positions(double cell_radius, double sphere_radius)
{
	std::vector<std::vector<double>> cells;
	int xc=0,yc=0,zc=0;
	double x_spacing= cell_radius*sqrt(3);
	double y_spacing= cell_radius*2;
	double z_spacing= cell_radius*sqrt(3);
	
	std::vector<double> tempPoint(3,0.0);
	// std::vector<double> cylinder_center(3,0.0);
	
	for(double z=-sphere_radius;z<sphere_radius;z+=z_spacing, zc++)
	{
		for(double x=-sphere_radius;x<sphere_radius;x+=x_spacing, xc++)
		{
			for(double y=-sphere_radius;y<sphere_radius;y+=y_spacing, yc++)
			{
				tempPoint[0]=x + (zc%2) * 0.5 * cell_radius;
				tempPoint[1]=y + (xc%2) * cell_radius;
				tempPoint[2]=z;
				
				if(sqrt(norm_squared(tempPoint))< sphere_radius)
				{ cells.push_back(tempPoint); }
			}
			
		}
	}
	return cells;
	
}

std::vector<std::vector<double>> create_cell_disc_positions(double cell_radius, double disc_radius)
{	 
	double cell_spacing = 0.95 * 2.0 * cell_radius; 
	
	double x = 0.0; 
	double y = 0.0; 
	double x_outer = 0.0;

	std::vector<std::vector<double>> positions;
	std::vector<double> tempPoint(3,0.0);
	
	int n = 0; 
	while( y < disc_radius )
	{
		x = 0.0; 
		if( n % 2 == 1 )
		{ x = 0.5 * cell_spacing; }
		x_outer = sqrt( disc_radius*disc_radius - y*y ); 
		
		while( x < x_outer )
		{
			tempPoint[0]= x; tempPoint[1]= y;	tempPoint[2]= 0.0;
			positions.push_back(tempPoint);			
			if( fabs( y ) > 0.01 )
			{
				tempPoint[0]= x; tempPoint[1]= -y;	tempPoint[2]= 0.0;
				positions.push_back(tempPoint);
			}
			if( fabs( x ) > 0.01 )
			{ 
				tempPoint[0]= -x; tempPoint[1]= y;	tempPoint[2]= 0.0;
				positions.push_back(tempPoint);
				if( fabs( y ) > 0.01 )
				{
					tempPoint[0]= -x; tempPoint[1]= -y;	tempPoint[2]= 0.0;
					positions.push_back(tempPoint);
				}
			}
			x += cell_spacing; 
		}		
		y += cell_spacing * sqrt(3.0)/2.0; 
		n++; 
	}
	return positions;
}

bool wait_for_cell_growth(Cell* pCell, Phenotype& phenotype, double dt){
	//std::cout << pCell->phenotype.intracellular->get_boolean_variable_value("Cell_growth");
		return !pCell->phenotype.intracellular->get_boolean_variable_value("Cell_growth");

}

/* Return if level of protein given by index around the cell is high enough (compared to given threshold) */
int feel_enough(std::string field, Cell* pCell)
{	
	int voxel_index = pCell->get_current_mechanics_voxel_index();
	//return local_density(field) > cell_line->prot_threshold; 
	int ind = BioFVM::microenvironment.find_density_index( field );
	if ( ind >= 0 )	
		return BioFVM::microenvironment.density_vector(voxel_index)[ind] > get_threshold(field); 
	return -1;
}

bool sense_light(Cell* pCell){
	int voxel_index = pCell->get_current_mechanics_voxel_index();
	//return local_density(field) > cell_line->prot_threshold; 
	int ind = BioFVM::microenvironment.find_density_index("light");
	if ( ind >= 0 )	
		return BioFVM::microenvironment.density_vector(voxel_index)[ind]; 
	return 0;
}

/*insert a mutation in a specified area of the tumor */
void start_SRC_mutation(bool light_on){

// Here we design a spherical shell 
 std::vector<double> center(3, 0);
 double light_radius = parameters.doubles("config_radius_light");
 //double outer_radius = 150;
 for (auto voxel : microenvironment.mesh.voxels) {
	 //std::cout << voxel.center;
	 // Compute norm to center
 	double t_norm = norm(voxel.center);
 	// If norm is in [inner_radius, outer_radius], then we add it
 	if(t_norm < light_radius && light_on){
 		microenvironment.density_vector(voxel.mesh_index)[microenvironment.find_density_index("light")] = 1;
 	}
 	else{
	 	microenvironment.density_vector(voxel.mesh_index)[microenvironment.find_density_index("light")] = 0;
 		}
 	}
}

	// FUNCTIONS TO PLOT CELLS

std::vector<std::string> ECM_coloring_function( Cell* pCell)
{
	std::vector< std::string > output( 4 , "black" );
	std::string parameter = parameters.strings("parameter_to_visualize");;
	double param = pCell->custom_data[parameter];
	int color = (int) round( param * 255.0 );
	if(color > 255){
		color = 255;
	}
	char szTempString [128];
	sprintf( szTempString , "rgb(%u,0,%u)", color, 255-color );
	output[0].assign( szTempString );
	return output;

}

std::vector<std::string> phase_coloring_function( Cell* pCell )
{
	std::vector< std::string > output( 4 , "rgb(0,0,0)" );

	if ( pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::Ki67_negative )
	{
		output[0] = "rgb(0,255,0)"; //green
		output[2] = "rgb(0,125,0)";
		
	}
	if ( pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::Ki67_positive_premitotic )
	{
		output[0] = "rgb(255,0,0)"; //red
		output[2] = "rgb(125,0,0)";
		
	}
	if ( pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::Ki67_positive_postmitotic )
	{
		output[0] = "rgb(255,255,0)"; //yellow
		output[2] = "rgb(125,125,0)";
		
	}
	if (pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic_swelling || 
		pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic_lysed || 
		pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::necrotic )
	{
		output[0] = "rgb(165,42,42)"; //brown
		output[2] = "rgb(165,42,42)";
	}
	if (pCell->phenotype.cycle.current_phase().code == PhysiCell_constants::apoptotic )  
	{
		output[0] = "rgb(0,0,0)";
		output[2] = "rgb(0,0,0)";
	}
	return output;
}

std::vector<std::string> node_coloring_function( Cell* pCell )
{
	std::vector< std::string > output( 4 , "rgb(0,0,0)" );
	//std::cout << pCell->phenotype.intracellular->get_boolean_node_value( parameters.strings("node_to_visualize"));
	if ( !pCell->phenotype.intracellular->get_boolean_variable_value( parameters.strings("node_to_visualize") ) ) //node off
	{
		output[0] = "rgb(0,0,255)"; //blue
		output[2] = "rgb(0,0,125)";
		
	}
	else{
		output[0] = "rgb(0,255,0)"; //green
		output[2] = "rgb(0,125,0)";
	}
	
	return output;
}


std::vector<std::string> my_coloring_function( Cell* pCell )
{
	
	 int color_number = parameters.ints("color_function");

	 if (color_number == 0)
	 	return ECM_coloring_function(pCell);
	 if (color_number == 1)
	 	return phase_coloring_function(pCell);
	 else 
	 	return node_coloring_function( pCell );
}

void SVG_plot_ecm( std::string filename , Microenvironment& M, double z_slice , double time, std::vector<std::string> (*cell_coloring_function)(Cell*), std::string sub )
{


	double X_lower = M.mesh.bounding_box[0];
	double X_upper = M.mesh.bounding_box[3];
 
	double Y_lower = M.mesh.bounding_box[1]; 
	double Y_upper = M.mesh.bounding_box[4]; 

	double plot_width = X_upper - X_lower; 
	double plot_height = Y_upper - Y_lower; 

	double font_size = 0.025 * plot_height; // PhysiCell_SVG_options.font_size; 
	double top_margin = font_size*(.2+1+.2+.9+.5 ); 

	// open the file, write a basic "header"
	std::ofstream os( filename , std::ios::out );
	if( os.fail() )
	{ 
		std::cout << std::endl << "Error: Failed to open " << filename << " for SVG writing." << std::endl << std::endl; 

		std::cout << std::endl << "Error: We're not writing data like we expect. " << std::endl
		<< "Check to make sure your save directory exists. " << std::endl << std::endl
		<< "I'm going to exit with a crash code of -1 now until " << std::endl 
		<< "you fix your directory. Sorry!" << std::endl << std::endl; 
		exit(-1); 
	} 
	
	Write_SVG_start( os, plot_width , plot_height + top_margin );

	// draw the background 
	Write_SVG_rect( os , 0 , 0 , plot_width, plot_height + top_margin , 0.002 * plot_height , "white", "white" );

	// write the simulation time to the top of the plot
 
	char* szString; 
	szString = new char [1024]; 
 
	int total_cell_count = all_cells->size(); 
 
	double temp_time = time; 

	std::string time_label = formatted_minutes_to_DDHHMM( temp_time ); 
 
	sprintf( szString , "Current time: %s, z = %3.2f %s", time_label.c_str(), 
		z_slice , PhysiCell_SVG_options.simulation_space_units.c_str() ); 
	Write_SVG_text( os, szString, font_size*0.5,  font_size*(.2+1), 
		font_size, PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() );
	sprintf( szString , "%u agents" , total_cell_count ); 
	Write_SVG_text( os, szString, font_size*0.5,  font_size*(.2+1+.2+.9), 
		0.95*font_size, PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() );
	
	delete [] szString; 


	// add an outer "g" for coordinate transforms 
	
	os << " <g id=\"tissue\" " << std::endl 
	   << "    transform=\"translate(0," << plot_height+top_margin << ") scale(1,-1)\">" << std::endl; 
	   
	// prepare to do mesh-based plot (later)
	
	double dx_stroma = M.mesh.dx; 
	double dy_stroma = M.mesh.dy; 
	double dz_stroma = M.mesh.dz;
	
	os << "  <g id=\"ECM\">" << std::endl; 
  
	int ratio = 1; 
	double voxel_size = dx_stroma / (double) ratio ; 
  
	double half_voxel_size = voxel_size / 2.0; 
	double normalizer = 78.539816339744831 / (voxel_size*voxel_size*voxel_size); 
	
	// color the dark background 

	for (int n = 0; n < M.number_of_voxels(); n++)
	{
		auto current_voxel = M.voxels(n);
		int z_center = current_voxel.center[2];
		double z_displ = z_center -  dz_stroma/2;
		
		double z_compare = z_displ;

		if (default_microenvironment_options.simulate_2D == true){
		z_compare = z_center;
		};

		if (z_slice == z_compare){
			int x_center = current_voxel.center[0];
			int y_center = current_voxel.center[1];
			
			double x_displ = x_center -  dx_stroma/2;
			double y_displ = (y_center - dy_stroma) +  dy_stroma/2;
			//std::cout <<  x_displ - X_lower << "  __  " << y_displ - Y_lower << "\n" ;
			int sub_index = M.find_density_index(sub);

			double concentration = M.density_vector(n)[sub_index];

			std::vector< std::string > output( 4 , "black" );
			int color = (int) round( concentration * 255.0 );
			if(color > 255){
				color = 255;
			}
			char szTempString [128];

			int green = 255 - color;
			int blue = 255 - color;
			int red = 255 - color;


			sprintf( szTempString , "rgb(%u, %u, %u)", red, green, blue );
			output[0].assign( szTempString );

			Write_SVG_rect( os , x_displ - X_lower , y_displ - Y_lower, dx_stroma, dy_stroma , 0 , "none", output[0] );
		}

	}

	// Write_SVG_rect( os , 0 , 0 , plot_width, plot_height , 0 , "none", "black" );

 
 // color in the background ECM
/* 
 if( ECM.TellRows() > 0 )
 {
  // find the k corresponding to z_slice
  
  
  
  Vector position; 
  *position(2) = z_slice; 
  

  // 25*pi* 5 microns^2 * length (in source) / voxelsize^3
  
  for( int j=0; j < ratio*ECM.TellCols() ; j++ )
  {
   // *position(1) = *Y_environment(j); 
   *position(1) = *Y_environment(0) - dy_stroma/2.0 + j*voxel_size + half_voxel_size; 
   
   for( int i=0; i < ratio*ECM.TellRows() ; i++ )
   {
    // *position(0) = *X_environment(i); 
    *position(0) = *X_environment(0) - dx_stroma/2.0 + i*voxel_size + half_voxel_size; 
	
    double E = evaluate_Matrix3( ECM, X_environment , Y_environment, Z_environment , position );	
	double BV = normalizer * evaluate_Matrix3( OxygenSourceHD, X_environment , Y_environment, Z_environment , position );
	if( isnan( BV ) )
	{ BV = 0.0; }

	vector<string> Colors;
	Colors = hematoxylin_and_eosin_stroma_coloring( E , BV );
	Write_SVG_rect( os , *position(0)-half_voxel_size-X_lower , *position(1)-half_voxel_size+top_margin-Y_lower, 
	voxel_size , voxel_size , 1 , Colors[0], Colors[0] );
   
   }
  }
 
 }
*/
	os << "  </g>" << std::endl; 

 
	// plot intersecting cells 
	os << "  <g id=\"cells\">" << std::endl; 


	double lowest_pressure = 1.0;
	double max_pressure = 1.0;
	for( int i=0 ; i < total_cell_count ; i++ )
	{
		Cell* pC = (*all_cells)[i]; // global_cell_list[i]; 

		double pressure = pC->custom_data["padhesion"];

		if (pressure < lowest_pressure)
			lowest_pressure = pressure;
		if (pressure > max_pressure)
			max_pressure = pressure;

		static std::vector<std::string> Colors; 
		if( fabs( (pC->position)[2] - z_slice ) < pC->phenotype.geometry.radius )
		{
			double r = pC->phenotype.geometry.radius ; 
			double rn = pC->phenotype.geometry.nuclear_radius ; 
			double z = fabs( (pC->position)[2] - z_slice) ; 
   
			Colors = cell_coloring_function( pC ); 

			os << "   <g id=\"cell" << pC->ID << "\">" << std::endl; 
  
			// figure out how much of the cell intersects with z = 0 
   
			double plot_radius = sqrt( r*r - z*z ); 

			Write_SVG_circle( os, (pC->position)[0]-X_lower, (pC->position)[1]-Y_lower, 
				plot_radius , 0.5, Colors[1], Colors[0] ); 

			// plot the nucleus if it, too intersects z = 0;
			if( fabs(z) < rn && PhysiCell_SVG_options.plot_nuclei == true )
			{   
				plot_radius = sqrt( rn*rn - z*z ); 
			 	Write_SVG_circle( os, (pC->position)[0]-X_lower, (pC->position)[1]-Y_lower, 
					plot_radius, 0.5, Colors[3],Colors[2]); 
			}					  
			os << "   </g>" << std::endl;
		}
	}

	std::cout << max_pressure << "  --  " << lowest_pressure;

	os << "  </g>" << std::endl; 
	
	// end of the <g ID="tissue">
	os << " </g>" << std::endl; 
 
	// draw a scale bar
 
	double bar_margin = 0.025 * plot_height; 
	double bar_height = 0.01 * plot_height; 
	double bar_width = PhysiCell_SVG_options.length_bar; 
	double bar_stroke_width = 0.001 * plot_height; 
	
	std::string bar_units = PhysiCell_SVG_options.simulation_space_units; 
	// convert from micron to mm
	double temp = bar_width;  

	if( temp > 999 && std::strstr( bar_units.c_str() , PhysiCell_SVG_options.mu.c_str() )   )
	{
		temp /= 1000;
		bar_units = "mm";
	}
	// convert from mm to cm 
	if( temp > 9 && std::strcmp( bar_units.c_str() , "mm" ) == 0 )
	{
		temp /= 10; 
		bar_units = "cm";
	}
	
	szString = new char [1024];
	sprintf( szString , "%u %s" , (int) round( temp ) , bar_units.c_str() );
 
	Write_SVG_rect( os , plot_width - bar_margin - bar_width  , plot_height + top_margin - bar_margin - bar_height , 
		bar_width , bar_height , 0.002 * plot_height , "rgb(255,255,255)", "rgb(0,0,0)" );
	Write_SVG_text( os, szString , plot_width - bar_margin - bar_width + 0.25*font_size , 
		plot_height + top_margin - bar_margin - bar_height - 0.25*font_size , 
		font_size , PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() ); 
	
	delete [] szString; 

	// plot runtime 
	szString = new char [1024]; 
	RUNTIME_TOC(); 
	std::string formatted_stopwatch_value = format_stopwatch_value( runtime_stopwatch_value() );
	Write_SVG_text( os, formatted_stopwatch_value.c_str() , bar_margin , top_margin + plot_height - bar_margin , 0.75 * font_size , 
		PhysiCell_SVG_options.font_color.c_str() , PhysiCell_SVG_options.font.c_str() );
	delete [] szString; 

	// draw a box around the plot window
	Write_SVG_rect( os , 0 , top_margin, plot_width, plot_height , 0.002 * plot_height , "rgb(0,0,0)", "none" );
	
	// close the svg tag, close the file
	Write_SVG_end( os ); 
	os.close();
 
	return; 
}