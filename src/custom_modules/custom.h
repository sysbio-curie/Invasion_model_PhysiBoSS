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
#ifndef __Custom_h__
#define __Custom_h__


#include "../core/PhysiCell.h"
#include "../modules/PhysiCell_standard_modules.h" 
#include "custom_main.h"

using namespace BioFVM; 
using namespace PhysiCell;

struct init_record
{
	float x;
	float y;
	float z;
	float radius;
	int phase;
	double elapsed_time;
};

///std::string ecm_file;
// setup functions to help us along 
void create_cell_types( void );
void setup_tissue( void ); 
//std::vector<std::string> conc_names;
// set up the BioFVM microenvironment 
void setup_microenvironment( void ); 
// custom pathology coloring function 
std::vector<std::string> my_coloring_function( Cell* );
std::vector<std::string> ECM_coloring_function( Cell*);
std::vector<std::string> phase_coloring_function( Cell* );
std::vector<std::string> node_coloring_function( Cell* );
void SVG_plot_ecm( std::string filename , Microenvironment& M, double z_slice , double time, std::vector<std::string> (*cell_coloring_function)(Cell*), std::string sub );

// custom cell phenotype functions could go here 
void tumor_cell_phenotype_with_signaling( Cell* pCell, Phenotype& phenotype, double dt );
/** \brief Write Density values to output file */
void set_input_nodes(Cell* pCell); 
void from_nodes_to_cell(Cell* pCell, Phenotype& phenotype, double dt);
std::vector<init_record> read_init_file(std::string filename, char delimiter, bool header);
void set_substrate_density(int density_index, double max, double min, double radius);
std::vector<std::vector<double>> create_cell_sphere_positions(double cell_radius, double sphere_radius);
std::vector<std::vector<double>> create_cell_disc_positions(double cell_radius, double disc_radius);
/** \brief Go to proliferative phase if proliferation ON and in G0 phase */
void do_proliferation(Cell* pCell, Phenotype& phenotype, double dt);
bool wait_for_cell_growth(Cell* pCell, Phenotype& phenotype, double dt);
bool waiting_to_remove(Cell* cell, Phenotype& phenotype, double dt);
inline float sphere_volume_from_radius(float radius) {return 4.0/3.0 * PhysiCell_constants::pi * std::pow(radius, 3);}

bool touch_ECM(Cell* pCell);
bool touch_TGFbeta(Cell* pCell);
void enough_to_node( Cell* pCell, std::string nody, std::string field );
void color_node(Cell* pCell);
inline void static_volume_function( Cell* pCell, Phenotype& phenotype, double dt ){return ;}; // do not update volume
	
/** \brief (De)-Activate ECM degradation by the cell */
void set_mmp( int activate );
	
/** \brief Change the current value of integrin percent coeff, increase or decrease according to up value */
inline void evolve_integrin_coef(Cell* pC, int up, double dt )
{ pC->custom_data["integrin"] = evolve_coef( up, pC->custom_data["integrin"], dt ); return ; };
	
/** \brief Change the current value of cell cell adhesion percent coeff, increase or decrease according to up value */
inline void evolve_cellcell_coef(Cell* pC, int up, double dt )
{pC->custom_data["padhesion"] = evolve_coef( up, pC->custom_data["padhesion"], dt ); return ; };

inline void evolve_motility_coef(Cell* pC, int up, double dt )
{pC->custom_data["pmotility"] = evolve_coef( up, pC->custom_data["pmotility"], dt); return ;}; //maybe both pmotility and padhseion to move?

void custom_cell_attach(Cell* pCell);

void custom_detach_cells(Cell* pCell);
	
/** \brief Get the current value of heterotypic adhesion strength */
inline double get_heterotypic_strength( double percent )
{ return current_value( PhysiCell::parameters.doubles("heterotypic_adhesion_min"), PhysiCell::parameters.doubles("heterotypic_adhesion_max"), percent ); };
	
/** \brief Get the current value of homotypic adhesion strength */
inline double get_homotypic_strength( double percent )
{ return current_value( PhysiCell::parameters.doubles("homotypic_adhesion_min"), PhysiCell::parameters.doubles("homotypic_adhesion_max"), percent ); };

/** \brief Get the current value of integrin strength */
inline double get_integrin_strength( double percent )
{ return current_value( PhysiCell::parameters.doubles("ecm_adhesion_min"), PhysiCell::parameters.doubles("ecm_adhesion_max"), percent ); };
	
/** \brief Get the current value of motility coefficient */
inline double get_motility_amplitude( double percent )
{ return current_value(PhysiCell::parameters.doubles("motility_amplitude_min"), PhysiCell::parameters.doubles("motility_amplitude_max"), percent ); };

/** \brief Return amount of contact with other cells */
inline double contact_cell(Cell* pCell)
	{ double contact =  pCell->custom_data["cell_contact"]; return contact; };

/** \brief (De)-Activate ECM degradation by the cell */
void set_mmp( Cell* pCell, int activate );
void freezer( Cell* pCell, int frozen );

double custom_adhesion_function(Cell* pCell, Cell* otherCell, double distance);
double custom_repulsion_function(Cell* pCell, Cell* otherCell);
/** \brief Set the value of freezed */
inline void freezing(Cell* pC, int frozen )
{ pC->custom_data["freezed"] = frozen; };

/** \brief Return amount of contact with ECM */
inline double contact_ecm(Cell* pCell)
{ double ecm_contact = pCell->custom_data["ecm_contact"]; return ecm_contact / pCell->phenotype.geometry.radius ; };

inline double contact_TGFB(Cell* pCell)
{ double tgfbeta_contact = pCell->custom_data["TGFbeta_contact"]; return tgfbeta_contact / pCell->phenotype.geometry.radius ; };

/** \brief Return value of adhesion strength with ECM according to integrin level */
double integrinStrength(Cell* pC);
double get_adhesion();
double adhesion(Cell* pCell, Cell* other_cell);
double get_adhesion();
void set_oxygen_motility(Cell* pCell, bool value);
bool has_neighbor(Cell* pCell, int);
bool wait_for_nucleus_growth(Cell* cell, Phenotype& phenotype, double dt);
void add_ecm_interaction( Cell* pCell, int index_ecm, int index_voxel );
void ecm_cell_function (Cell* cell, Phenotype& phenotype, double dt);
void add_TGFbeta_interaction(Cell* pC, int index_voxel);
bool necrotic_oxygen(Cell* pCell);
void custom_update_velocity( Cell* pCell, Phenotype& phenotype, double dt);
int feel_enough(std::string field, Cell* pCell);
void start_SRC_mutation(bool light_on);
bool sense_light(Cell* pCell);
#endif