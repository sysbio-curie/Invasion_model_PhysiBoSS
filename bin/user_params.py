 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name2 = Button(description='substrate_to_monitor', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.substrate_to_monitor = Text(
          value='ecm',
          style=style, layout=widget_layout)

        param_name39 = Button(description='node_to_mutate', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'lightblue'

        self.node_to_mutate = Text(
            value='SRC',
            style=style, layout=widget_layout)

        param_name3 = Button(description='src_activation_time', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.src_activation_time = FloatText(
          value=120,
          step=10,
          style=style, layout=widget_layout)

        param_name4 = Button(description='src_stop_time', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.src_stop_time = FloatText(
          value=1440,
          step=100,
          style=style, layout=widget_layout)

        param_name5 = Button(description='config_radius_light', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.config_radius_light = FloatText(
          value=15,
          step=1,
          style=style, layout=widget_layout)

        param_name6 = Button(description='ecm_adhesion_min', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.ecm_adhesion_min = FloatText(
          value= 1 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='ecm_adhesion_max', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.ecm_adhesion_max = FloatText(
          value= 2 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='cell_ecm_repulsion', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.cell_ecm_repulsion = FloatText(
          value= 7 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='choose_adhesion_function', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.choose_adhesion_function = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='cell_radius', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.cell_radius = FloatText(
          value= 8.413 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='max_interaction_factor', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.max_interaction_factor = FloatText(
          value= 1.3 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='homotypic_adhesion_min', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.homotypic_adhesion_min = FloatText(
          value= 0.4 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='homotypic_adhesion_max', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.homotypic_adhesion_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='heterotypic_adhesion_min', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.heterotypic_adhesion_min = FloatText(
          value= 0.4 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='heterotypic_adhesion_max', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.heterotypic_adhesion_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='contact_cell_ECM_threshold', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.contact_cell_ECM_threshold = FloatText(
          value= 0.05 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name17 = Button(description='contact_TGFB_threshold', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.contact_TGFB_threshold = FloatText(
          value= 0.02 ,
          step=0.001,
          style=style, layout=widget_layout)

        param_name18 = Button(description='contact_cell_cell_threshold', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.contact_cell_cell_threshold = FloatText(
          value= 0.3 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name19 = Button(description='cell_junctions_attach_threshold', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.cell_junctions_attach_threshold = FloatText(
          value=1.1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name20 = Button(description='cell_junctions_detach_threshold', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.cell_junctions_detach_threshold = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.migration_bias = FloatText(
          value=0.8,
          step=0.1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='migration_speed', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.migration_speed = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name23 = Button(description='persistence', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.persistence = FloatText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name24 = Button(description='motility_amplitude_min', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.motility_amplitude_min = FloatText(
          value= 0.1 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name25 = Button(description='motility_amplitude_max', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.motility_amplitude_max = FloatText(
          value= 0.8 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name26 = Button(description='mode_motility', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.mode_motility = IntText(
          value= 1 ,
          step=0.1,
          style=style, layout=widget_layout)

        param_name27 = Button(description='config_radius', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.config_radius = FloatText(
          value=100,
          step=10,
          style=style, layout=widget_layout)

        param_name28 = Button(description='tgfbeta_radius', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.tgfbeta_radius = FloatText(
          value=90,
          step=1,
          style=style, layout=widget_layout)

        param_name29 = Button(description='density_tgfbeta_max', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.density_tgfbeta_max = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name30 = Button(description='density_tgfbeta_min', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.density_tgfbeta_min = FloatText(
          value=0.4,
          step=0.1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='density_ECM_max', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.density_ECM_max = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name32 = Button(description='density_ECM_min', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.density_ECM_min = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name33 = Button(description='ecm_degradation', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.ecm_degradation = FloatText(
          value= 0.05 ,
          step=0.01,
          style=style, layout=widget_layout)

        param_name34 = Button(description='TGFbeta_degradation', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.TGFbeta_degradation = FloatText(
          value= 0.002 ,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name35 = Button(description='ECM_TGFbeta_ratio', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.ECM_TGFbeta_ratio = FloatText(
          value=0.75,
          step=0.1,
          style=style, layout=widget_layout)

        param_name36 = Button(description='parameter_to_visualize', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.parameter_to_visualize = Text(
          value='padhesion',
          style=style, layout=widget_layout)

        param_name37 = Button(description='node_to_visualize', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.node_to_visualize = Text(
          value='EMT',
          style=style, layout=widget_layout)

        param_name38 = Button(description='color_function', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.color_function = IntText(
          value=2,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='micron/min', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='min', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'
        units_button38 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'tan'
        units_button39 = Button(description='', disabled=True, layout=units_button_layout)
        units_button39.style.button_color = 'lightblue'

        desc_button1 = Button(description='change seed of the simulation' , tooltip='change seed of the simulation', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='change the initial radius of the light illumination' , tooltip='change the initial radius of the light illumination', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='used to set the min adhesion between cells and ECM' , tooltip='used to set the min adhesion between cells and ECM', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='used to set the min adhesion between cells and ECM' , tooltip='used to set the min adhesion between cells and ECM', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='change the value of ECM repulsion' , tooltip='change the value of ECM repulsion', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='switch between default adhesion function or custom' , tooltip='switch between default adhesion function or custom', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='initial radius of the cells' , tooltip='initial radius of the cells', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='used to set the max distance of interaction' , tooltip='used to set the max distance of interaction', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='not used yet' , tooltip='not used yet', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='not used yet' , tooltip='not used yet', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='used to set the min adhesion between cells of the same type' , tooltip='used to set the min adhesion between cells of the same type', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='used to set the max adhesion between cells of the same type' , tooltip='used to set the max adhesion between cells of the same type', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='change the threshold needed to trigger ECM interaction' , tooltip='change the threshold needed to trigger ECM interaction', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='change the threshold needed to trigger TGFbeta interaction' , tooltip='change the threshold needed to trigger TGFbeta interaction', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='change the threshold needed to trigger Neighbours and Neigh2 node' , tooltip='change the threshold needed to trigger Neighbours and Neigh2 node', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='change the threshold needed to attach cells in cluster with cell junction' , tooltip='change the threshold needed to attach cells in cluster with cell junction', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='change the threshold needed to detach cells in cluster with cell junction' , tooltip='change the threshold needed to detach cells in cluster with cell junction', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='change value of migration bias for cells with migration node active' , tooltip='change value of migration bias for cells with migration node active', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='change value of migration speed for cells with migration node active' , tooltip='change value of migration speed for cells with migration node active', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='change value of persistence for cells with migration node active' , tooltip='change value of persistence for cells with migration node active', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='change the min value of motility amplitude' , tooltip='change the min value of motility amplitude', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='change the max value of motility amplitude' , tooltip='change the max value of motility amplitude', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='not used yet' , tooltip='not used yet', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='change the initial radius of the tumor' , tooltip='change the initial radius of the tumor', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='change radius of the tgfbeta substrate' , tooltip='change radius of the tgfbeta substrate', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='change initial density of the tgfbeta substrate' , tooltip='change initial density of the tgfbeta substrate', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='change initial density of the tgfbeta substrate' , tooltip='change initial density of the tgfbeta substrate', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='change initial density of the ECM substrate' , tooltip='change initial density of the ECM substrate', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='change initial density of the ECM substrate' , tooltip='change initial density of the ECM substrate', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='chenage the amount of ECM degraded by the cells with Matrix_modifcation ON' , tooltip='chenage the amount of ECM degraded by the cells with Matrix_modifcation ON', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='chenage the amount of TGFbeta degraded by the cells' , tooltip='chenage the amount of TGFbeta degraded by the cells', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='change the threshold needed to start sensing TGFbeta inside a voxel with ECM (cell must degrades a certain amount of ECM before sensing TGFbeta)' , tooltip='change the threshold needed to start sensing TGFbeta inside a voxel with ECM (cell must degrades a certain amount of ECM before sensing TGFbeta)', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='change the parameter to visualize in the plot tab when coloring cells by custom data value' , tooltip='change the parameter to visualize in the plot tab when coloring cells by custom data value', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='change the node to visualize in the plot tab when coloring cells by custom data value' , tooltip='change the node to visualize in the plot tab when coloring cells by custom data value', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='change the basic color function: 0 for ECM based color, 1 for phase based color, 2 for node based color' , tooltip='change the basic color function: 0 for ECM based color, 1 for phase based color, 2 for node based color', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='select another node to mutate for the experiments in a selected area ' , tooltip='select another node to mutate for the experiments in a selected area', disabled=True, layout=desc_button_layout)
        desc_button39.style.button_color = 'lightblue'


        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row2 = [param_name2, self.substrate_to_monitor, units_button2, desc_button2] 
        row3 = [param_name3, self.src_activation_time, units_button3, desc_button3] 
        row4 = [param_name4, self.src_stop_time, units_button4, desc_button4] 
        row5 = [param_name5, self.config_radius_light, units_button5, desc_button5] 
        row6 = [param_name6, self.ecm_adhesion_min, units_button6, desc_button6] 
        row7 = [param_name7, self.ecm_adhesion_max, units_button7, desc_button7] 
        row8 = [param_name8, self.cell_ecm_repulsion, units_button8, desc_button8] 
        row9 = [param_name9, self.choose_adhesion_function, units_button9, desc_button9] 
        row10 = [param_name10, self.cell_radius, units_button10, desc_button10] 
        row11 = [param_name11, self.max_interaction_factor, units_button11, desc_button11] 
        row12 = [param_name12, self.homotypic_adhesion_min, units_button12, desc_button12] 
        row13 = [param_name13, self.homotypic_adhesion_max, units_button13, desc_button13] 
        row14 = [param_name14, self.heterotypic_adhesion_min, units_button14, desc_button14] 
        row15 = [param_name15, self.heterotypic_adhesion_max, units_button15, desc_button15] 
        row16 = [param_name16, self.contact_cell_ECM_threshold, units_button16, desc_button16] 
        row17 = [param_name17, self.contact_TGFB_threshold, units_button17, desc_button17] 
        row18 = [param_name18, self.contact_cell_cell_threshold, units_button18, desc_button18] 
        row19 = [param_name19, self.cell_junctions_attach_threshold, units_button19, desc_button19] 
        row20 = [param_name20, self.cell_junctions_detach_threshold, units_button20, desc_button20] 
        row21 = [param_name21, self.migration_bias, units_button21, desc_button21] 
        row22 = [param_name22, self.migration_speed, units_button22, desc_button22] 
        row23 = [param_name23, self.persistence, units_button23, desc_button23] 
        row24 = [param_name24, self.motility_amplitude_min, units_button24, desc_button24] 
        row25 = [param_name25, self.motility_amplitude_max, units_button25, desc_button25] 
        row26 = [param_name26, self.mode_motility, units_button26, desc_button26] 
        row27 = [param_name27, self.config_radius, units_button27, desc_button27] 
        row28 = [param_name28, self.tgfbeta_radius, units_button28, desc_button28] 
        row29 = [param_name29, self.density_tgfbeta_max, units_button29, desc_button29] 
        row30 = [param_name30, self.density_tgfbeta_min, units_button30, desc_button30] 
        row31 = [param_name31, self.density_ECM_max, units_button31, desc_button31] 
        row32 = [param_name32, self.density_ECM_min, units_button32, desc_button32] 
        row33 = [param_name33, self.ecm_degradation, units_button33, desc_button33] 
        row34 = [param_name34, self.TGFbeta_degradation, units_button34, desc_button34] 
        row35 = [param_name35, self.ECM_TGFbeta_ratio, units_button35, desc_button35] 
        row36 = [param_name36, self.parameter_to_visualize, units_button36, desc_button36] 
        row37 = [param_name37, self.node_to_visualize, units_button37, desc_button37] 
        row38 = [param_name38, self.color_function, units_button38, desc_button38]
        row39 = [param_name39, self.node_to_mutate, units_button39, desc_button39]

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box39,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.substrate_to_monitor.value = (uep.find('.//substrate_to_monitor').text)
        self.node_to_mutate.value = (uep.find('.//node_to_mutate').text)
        self.src_activation_time.value = float(uep.find('.//src_activation_time').text)
        self.src_stop_time.value = float(uep.find('.//src_stop_time').text)
        self.config_radius_light.value = float(uep.find('.//config_radius_light').text)
        self.ecm_adhesion_min.value = float(uep.find('.//ecm_adhesion_min').text)
        self.ecm_adhesion_max.value = float(uep.find('.//ecm_adhesion_max').text)
        self.cell_ecm_repulsion.value = float(uep.find('.//cell_ecm_repulsion').text)
        self.choose_adhesion_function.value = int(uep.find('.//choose_adhesion_function').text)
        self.cell_radius.value = float(uep.find('.//cell_radius').text)
        self.max_interaction_factor.value = float(uep.find('.//max_interaction_factor').text)
        self.homotypic_adhesion_min.value = float(uep.find('.//homotypic_adhesion_min').text)
        self.homotypic_adhesion_max.value = float(uep.find('.//homotypic_adhesion_max').text)
        self.heterotypic_adhesion_min.value = float(uep.find('.//heterotypic_adhesion_min').text)
        self.heterotypic_adhesion_max.value = float(uep.find('.//heterotypic_adhesion_max').text)
        self.contact_cell_ECM_threshold.value = float(uep.find('.//contact_cell_ECM_threshold').text)
        self.contact_TGFB_threshold.value = float(uep.find('.//contact_TGFB_threshold').text)
        self.contact_cell_cell_threshold.value = float(uep.find('.//contact_cell_cell_threshold').text)
        self.cell_junctions_attach_threshold.value = float(uep.find('.//cell_junctions_attach_threshold').text)
        self.cell_junctions_detach_threshold.value = float(uep.find('.//cell_junctions_detach_threshold').text)
        self.migration_bias.value = float(uep.find('.//migration_bias').text)
        self.migration_speed.value = float(uep.find('.//migration_speed').text)
        self.persistence.value = float(uep.find('.//persistence').text)
        self.motility_amplitude_min.value = float(uep.find('.//motility_amplitude_min').text)
        self.motility_amplitude_max.value = float(uep.find('.//motility_amplitude_max').text)
        self.mode_motility.value = int(uep.find('.//mode_motility').text)
        self.config_radius.value = float(uep.find('.//config_radius').text)
        self.tgfbeta_radius.value = float(uep.find('.//tgfbeta_radius').text)
        self.density_tgfbeta_max.value = float(uep.find('.//density_tgfbeta_max').text)
        self.density_tgfbeta_min.value = float(uep.find('.//density_tgfbeta_min').text)
        self.density_ECM_max.value = float(uep.find('.//density_ECM_max').text)
        self.density_ECM_min.value = float(uep.find('.//density_ECM_min').text)
        self.ecm_degradation.value = float(uep.find('.//ecm_degradation').text)
        self.TGFbeta_degradation.value = float(uep.find('.//TGFbeta_degradation').text)
        self.ECM_TGFbeta_ratio.value = float(uep.find('.//ECM_TGFbeta_ratio').text)
        self.parameter_to_visualize.value = (uep.find('.//parameter_to_visualize').text)
        self.node_to_visualize.value = (uep.find('.//node_to_visualize').text)
        self.color_function.value = int(uep.find('.//color_function').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//substrate_to_monitor').text = str(self.substrate_to_monitor.value)
        uep.find('.//node_to_mutate').text = str(self.node_to_mutate.value)
        uep.find('.//src_activation_time').text = str(self.src_activation_time.value)
        uep.find('.//src_stop_time').text = str(self.src_stop_time.value)
        uep.find('.//config_radius_light').text = str(self.config_radius_light.value)
        uep.find('.//ecm_adhesion_min').text = str(self.ecm_adhesion_min.value)
        uep.find('.//ecm_adhesion_max').text = str(self.ecm_adhesion_max.value)
        uep.find('.//cell_ecm_repulsion').text = str(self.cell_ecm_repulsion.value)
        uep.find('.//choose_adhesion_function').text = str(self.choose_adhesion_function.value)
        uep.find('.//cell_radius').text = str(self.cell_radius.value)
        uep.find('.//max_interaction_factor').text = str(self.max_interaction_factor.value)
        uep.find('.//homotypic_adhesion_min').text = str(self.homotypic_adhesion_min.value)
        uep.find('.//homotypic_adhesion_max').text = str(self.homotypic_adhesion_max.value)
        uep.find('.//heterotypic_adhesion_min').text = str(self.heterotypic_adhesion_min.value)
        uep.find('.//heterotypic_adhesion_max').text = str(self.heterotypic_adhesion_max.value)
        uep.find('.//contact_cell_ECM_threshold').text = str(self.contact_cell_ECM_threshold.value)
        uep.find('.//contact_TGFB_threshold').text = str(self.contact_TGFB_threshold.value)
        uep.find('.//contact_cell_cell_threshold').text = str(self.contact_cell_cell_threshold.value)
        uep.find('.//cell_junctions_attach_threshold').text = str(self.cell_junctions_attach_threshold.value)
        uep.find('.//cell_junctions_detach_threshold').text = str(self.cell_junctions_detach_threshold.value)
        uep.find('.//migration_bias').text = str(self.migration_bias.value)
        uep.find('.//migration_speed').text = str(self.migration_speed.value)
        uep.find('.//persistence').text = str(self.persistence.value)
        uep.find('.//motility_amplitude_min').text = str(self.motility_amplitude_min.value)
        uep.find('.//motility_amplitude_max').text = str(self.motility_amplitude_max.value)
        uep.find('.//mode_motility').text = str(self.mode_motility.value)
        uep.find('.//config_radius').text = str(self.config_radius.value)
        uep.find('.//tgfbeta_radius').text = str(self.tgfbeta_radius.value)
        uep.find('.//density_tgfbeta_max').text = str(self.density_tgfbeta_max.value)
        uep.find('.//density_tgfbeta_min').text = str(self.density_tgfbeta_min.value)
        uep.find('.//density_ECM_max').text = str(self.density_ECM_max.value)
        uep.find('.//density_ECM_min').text = str(self.density_ECM_min.value)
        uep.find('.//ecm_degradation').text = str(self.ecm_degradation.value)
        uep.find('.//TGFbeta_degradation').text = str(self.TGFbeta_degradation.value)
        uep.find('.//ECM_TGFbeta_ratio').text = str(self.ECM_TGFbeta_ratio.value)
        uep.find('.//parameter_to_visualize').text = str(self.parameter_to_visualize.value)
        uep.find('.//node_to_visualize').text = str(self.node_to_visualize.value)
        uep.find('.//color_function').text = str(self.color_function.value)
