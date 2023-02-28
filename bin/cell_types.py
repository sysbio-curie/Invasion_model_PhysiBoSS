 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box,Dropdown
import xml.etree.ElementTree as ET
    
class CellTypesTab(object):

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
        widget_layout_long = {'width': '20%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}
        divider_button_layout={'width':'60%'}
        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')

        self.cell_type_dropdown = Dropdown(description='Cell type:',)
        self.cell_type_dropdown.style = {'description_width': '%sch' % str(len(self.cell_type_dropdown.description) + 1)}

        cell_type_names_layout={'width':'30%'}
        cell_type_names_style={'description_width':'initial'}
        self.parent_name = Text(value='None',description='inherits properties from parent type:',disabled=True, style=cell_type_names_style, layout=cell_type_names_layout)

        explain_inheritance = Label(value='    This cell line inherits its properties from its parent type. Any settings below override those inherited properties.')  # , style=cell_type_names_style, layout=cell_type_names_layout)

        self.cell_type_parent_row = HBox([self.cell_type_dropdown, self.parent_name])
        self.cell_type_parent_dict = {}

        self.cell_type_dict = {}
        self.cell_type_dict['default'] = 'default'
        self.cell_type_dropdown.options = self.cell_type_dict

        self.cell_type_dropdown.observe(self.cell_type_cb)

        self.cell_type_parent_dict['default'] = 'None'


        self.cell_def_vboxes = []

        self.bnd_filenames = [None]*1

        self.cfg_filenames = [None]*1
        #  >>>>>>>>>>>>>>>>> <cell_definition> = default
        #  ------------------------- 
        div_row1 = Button(description='phenotype:cycle (model: advanced_Ki67_cycle_model; code=0)', disabled=True, layout=divider_button_layout)
        div_row1.style.button_color = 'orange'
        name_btn = Button(description='Phase 1 -> Phase 2 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float0 = FloatText(value='1e30', step='100000000000000000000000000000', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float0, units_btn, ]
        box0 = Box(children=row, layout=box_layout)

        name_btn = Button(description='Phase 2 -> Phase 0 transition rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float1 = FloatText(value='0.006666667', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float1, units_btn, ]
        box1 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row2 = Button(description='phenotype:death', disabled=True, layout=divider_button_layout)
        div_row2.style.button_color = 'orange'
        death_model1 = Button(description='model: apoptosis', disabled=True, layout={'width':'30%'})
        death_model1.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float2 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float2, units_btn, ]
        box2 = Box(children=row, layout=box_layout)

        death_model2 = Button(description='model: necrosis', disabled=True, layout={'width':'30%'})
        death_model2.style.button_color = '#ffde6b'
        name_btn = Button(description='death rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float3 = FloatText(value='0.0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float3, units_btn, ]
        box3 = Box(children=row, layout=box_layout)

        name_btn = Button(description='unlysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float4 = FloatText(value='0.05', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float4, units_btn, ]
        box4 = Box(children=row, layout=box_layout)

        name_btn = Button(description='lysed_fluid_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float5 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float5, units_btn, ]
        box5 = Box(children=row, layout=box_layout)

        name_btn = Button(description='cytoplasmic_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float6 = FloatText(value='1.66667e-02', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float6, units_btn, ]
        box6 = Box(children=row, layout=box_layout)

        name_btn = Button(description='nuclear_biomass_change_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float7 = FloatText(value='5.83333e-03', step='0.001', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float7, units_btn, ]
        box7 = Box(children=row, layout=box_layout)

        name_btn = Button(description='calcification_rate', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float8 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float8, units_btn, ]
        box8 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_rupture_volume', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float9 = FloatText(value='2.0', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float9, units_btn, ]
        box9 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row3 = Button(description='phenotype:mechanics', disabled=True, layout=divider_button_layout)
        div_row3.style.button_color = 'orange'
        name_btn = Button(description='cell_cell_repulsion_strength', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float10 = FloatText(value='20.0', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float10, units_btn, ]
        box10 = Box(children=row, layout=box_layout)

        name_btn = Button(description='relative_maximum_adhesion_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float11 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float11, units_btn, ]
        box11 = Box(children=row, layout=box_layout)

        self.bool0 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        name_btn = Button(description='set_relative_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float12 = FloatText(value='1.25', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [self.bool0, name_btn, self.float12, units_btn, ]
        box12 = Box(children=row, layout=box_layout)

        self.bool1 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        name_btn = Button(description='set_absolute_equilibrium_distance', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float13 = FloatText(value='10.12', step='1', style=style, layout=widget_layout)
        units_btn = Button(description='1/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [self.bool1, name_btn, self.float13, units_btn, ]
        box13 = Box(children=row, layout=box_layout)

        #  ------------------------- 
        div_row4 = Button(description='phenotype:motility', disabled=True, layout=divider_button_layout)
        div_row4.style.button_color = 'orange'

        name_btn = Button(description='speed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float14 = FloatText(value='0.3', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='micron/min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float14, units_btn]
        box14 = Box(children=row, layout=box_layout)

        name_btn = Button(description='persistence_time', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float15 = FloatText(value='0.3', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='min', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        row = [name_btn, self.float15, units_btn]
        box15 = Box(children=row, layout=box_layout)

        name_btn = Button(description='migration_bias', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float16 = FloatText(value='0.3', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='dimensionless', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float16, units_btn]
        box16 = Box(children=row, layout=box_layout)
        self.bool2 = Checkbox(description='enabled', value=True,layout=name_button_layout)
        self.bool3 = Checkbox(description='use_2D', value=False,layout=name_button_layout)
        #  ------------------------- 
        div_row5 = Button(description='phenotype:intracellular (maboss)', disabled=True, layout=divider_button_layout)
        div_row5.style.button_color = 'orange'
        bnd_filename = Button(description='bnd_filename', disabled=True, layout=name_button_layout)
        bnd_filename.style.button_color = 'tan'
        self.bnd_filenames[0] = Text(value='../data/boolean_network/intracellular_model.bnd', style=style, layout=widget_layout)
        row = [bnd_filename, self.bnd_filenames[0]]
        box17 = Box(children=row, layout=box_layout)
        cfg_filename = Button(description='cfg_filename', disabled=True, layout=name_button_layout)
        cfg_filename.style.button_color = 'lightgreen'
        self.cfg_filenames[0] = Text(value='../data/boolean_network/intracellular_model.cfg', style=style, layout=widget_layout)
        row = [cfg_filename, self.cfg_filenames[0]]
        box18 = Box(children=row, layout=box_layout)
        time_step = Button(description='time_step', disabled=True, layout=name_button_layout)
        time_step.style.button_color = 'tan'
        self.float17 = FloatText(value='10', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        row = [time_step, self.float17, units_btn]
        box19 = Box(children=row, layout=box_layout)

        # ---------------------------------------------------
        #INITIAL VALUES

        self.bool4 = Checkbox(description='enabled', value=True, layout=name_button_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width':'30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='GF', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float18 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool4, name_btn, self.float18, units_btn, ]
        box20 = Box(children=time_step, layout=box_layout)

        self.bool5 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width': '30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='ECM', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float19 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool5, name_btn, self.float19, units_btn, ]
        box21 = Box(children=time_step, layout=box_layout)

        self.bool6 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width': '30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='Oxy', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float20 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool6, name_btn, self.float18, units_btn, ]
        box22 = Box(children=time_step, layout=box_layout)

        self.bool7 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width': '30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='Neigh', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float21 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool7, name_btn, self.float21, units_btn, ]
        box23 = Box(children=time_step, layout=box_layout)

        self.bool8 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width': '30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='TGFbeta', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float22 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool8, name_btn, self.float22, units_btn, ]
        box24 = Box(children=time_step, layout=box_layout)

        self.bool9 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        intracellular_initial_values = Button(description='initial_values', disabled=True, layout={'width': '30%'})
        intracellular_initial_values.style.button_color = '#ffde6b'
        name_btn = Button(description='DNAdamage', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float23 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool9, name_btn, self.float23, units_btn, ]
        box25 = Box(children=time_step, layout=box_layout)

        # ---------------------------------------------------
        #MUTATIONS

        intracellular_mutations = Button(description='mutations', disabled=True, layout={'width':'30%'})
        intracellular_mutations.style.button_color = '#ffde6b'
        self.bool10 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='CTNNB1', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float24 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool10, name_btn, self.float24, units_btn, ]
        box26 = Box(children=time_step, layout=box_layout)

        self.bool11 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='p53', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float25 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool11, name_btn, self.float25, units_btn, ]
        box27 = Box(children=time_step, layout=box_layout)

        self.bool12 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='p63', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float26 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool12, name_btn, self.float26, units_btn, ]
        box28 = Box(children=time_step, layout=box_layout)

        self.bool13 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='MMPs', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float27 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool13, name_btn, self.float27, units_btn, ]
        box29 = Box(children=time_step, layout=box_layout)

        self.bool14 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='p73', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float28 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool14, name_btn, self.float28, units_btn, ]
        box30 = Box(children=time_step, layout=box_layout)

        self.bool15 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='miR34', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float29 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool15, name_btn, self.float29, units_btn, ]
        box31 = Box(children=time_step, layout=box_layout)

        self.bool16 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='AKT1', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float30 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool16, name_btn, self.float30, units_btn, ]
        box32 = Box(children=time_step, layout=box_layout)

        self.bool17 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='ERK', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float31 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool17, name_btn, self.float31, units_btn, ]
        box33 = Box(children=time_step, layout=box_layout)

        self.bool18 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='miR200', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float32 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool18, name_btn, self.float32, units_btn, ]
        box34 = Box(children=time_step, layout=box_layout)

        self.bool19 = Checkbox(description='enabled', value=False, layout=name_button_layout)
        name_btn = Button(description='miR203', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float33 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        time_step = [self.bool19, name_btn, self.float33, units_btn, ]
        box35 = Box(children=time_step, layout=box_layout)

#      ================== <custom_data>, if present ==================

        div_row6 = Button(description='Custom Data',disabled=True, layout=divider_button_layout)
        div_row6.style.button_color = 'cyan'
        # name_btn = Button(description='pintegrin', disabled=True, layout=name_button_layout)
        # name_btn.style.button_color = 'tan'
        # self.float32 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        # units_btn = Button(description='', disabled=True, layout=name_button_layout)
        # units_btn.style.button_color = 'tan'
        # description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        # description_btn.style.button_color = 'tan'
        # row = [name_btn, self.float32, units_btn, description_btn]

        # box34 = Box(children=row, layout=box_layout)
        # name_btn = Button(description='integrin', disabled=True, layout=name_button_layout)
        # name_btn.style.button_color = 'lightgreen'
        # self.float33 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        # units_btn = Button(description='', disabled=True, layout=name_button_layout)
        # units_btn.style.button_color = 'lightgreen'
        # description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        # description_btn.style.button_color = 'lightgreen'
        # row = [name_btn, self.float33, units_btn, description_btn]
        #
        # box35 = Box(children=row, layout=box_layout)
        # name_btn = Button(description='pmotility', disabled=True, layout=name_button_layout)
        # name_btn.style.button_color = 'tan'
        # self.float34 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        # units_btn = Button(description='', disabled=True, layout=name_button_layout)
        # units_btn.style.button_color = 'tan'
        # description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        # description_btn.style.button_color = 'tan'
        # row = [name_btn, self.float34, units_btn, description_btn]

        box36 = Box(children=row, layout=box_layout)
        name_btn = Button(description='padhesion', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float35 = FloatText(value='0.1', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float35, units_btn, description_btn]

        box37 = Box(children=row, layout=box_layout)
        name_btn = Button(description='nucleus_deform', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float36 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float36, units_btn, description_btn]

        box38 = Box(children=row, layout=box_layout)
        name_btn = Button(description='ecm_contact', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float37 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float37, units_btn, description_btn]

        box39 = Box(children=row, layout=box_layout)
        name_btn = Button(description='TGFbeta_contact', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float38 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float38, units_btn, description_btn]

        box40 = Box(children=row, layout=box_layout)
        name_btn = Button(description='cell_contact', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float39 = FloatText(value='0.6', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float39, units_btn, description_btn]

        box41 = Box(children=row, layout=box_layout)
        name_btn = Button(description='freezed', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'tan'
        self.float40 = FloatText(value='0', step='0.01', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'tan'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'tan'
        row = [name_btn, self.float40, units_btn, description_btn]

        box42 = Box(children=row, layout=box_layout)
        name_btn = Button(description='passive', disabled=True, layout=name_button_layout)
        name_btn.style.button_color = 'lightgreen'
        self.float41 = FloatText(value='1', step='0.1', style=style, layout=widget_layout)
        units_btn = Button(description='', disabled=True, layout=name_button_layout)
        units_btn.style.button_color = 'lightgreen'
        description_btn = Button(description='', disabled=True, layout=desc_button_layout)
        description_btn.style.button_color = 'lightgreen'
        row = [name_btn, self.float41, units_btn, description_btn]

        box43 = Box(children=row, layout=box_layout)

        self.cell_def_vbox0 = VBox([
          div_row1, box0, box1, div_row2, death_model1,box2, death_model2,box3, box4, box5, box6, box7, box8, box9, div_row3, box10, box11, box12, box13, div_row4, box14,box15,box16,self.bool2,self.bool3,div_row5, box17,box18,box19,intracellular_initial_values,box20, box21,
          box22,
          box23,
          box24,
          box25, intracellular_mutations,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35
        ])

        # custom data: div_row6,
        #           box34,
        #           box35,
        #           box36, box37, box38, box39, box40, box41, box42, box43

        # ------------------------------------------
        self.cell_def_vboxes.append(self.cell_def_vbox0)



        row = [name_btn, self.float28, units_btn, description_btn] 
        box20 = Box(children=time_step, layout=box_layout)


        self.tab = VBox([
          self.cell_type_parent_row, explain_inheritance, 
self.cell_def_vbox0,         ])
        self.display_cell_type_default()

    #------------------------------
    def cell_type_cb(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print("changed to %s" % change['new'])
            self.parent_name.value = self.cell_type_parent_dict[change['new']]
            idx_selected = list(self.cell_type_parent_dict.keys()).index(change['new'])
            # print('index=',idx_selected)
            # self.vbox1.layout.visibility = 'hidden'  # vs. visible
            # self.vbox1.layout.visibility = None 

            # There's probably a better way to do this, but for now,
            # we hide all vboxes containing the widgets for the different cell defs
            # and only display the contents of the selected one.
            for vb in self.cell_def_vboxes:
                vb.layout.display = 'none'   # vs. 'contents'
            self.cell_def_vboxes[idx_selected].layout.display = 'contents'   # vs. 'contents'


    #------------------------------
    def display_cell_type_default(self):
        # print("display_cell_type_default():")
        #print("    self.cell_type_parent_dict = ",self.cell_type_parent_dict)

        # There's probably a better way to do this, but for now,
        # we hide all vboxes containing the widgets for the different cell defs
        # and only display the contents of 'default'
        for vb in self.cell_def_vboxes:
            vb.layout.display = 'none'   # vs. 'contents'
        self.cell_def_vboxes[0].layout.display = 'contents'


    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (advanced_Ki67_cycle_model)
        self.float0.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text)
        self.float1.value = float(uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text)
        # ---------  death 
        self.float2.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text)
        self.float3.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text)
        self.float4.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text)
        self.float5.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text)
        self.float6.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text)
        self.float7.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text)
        self.float8.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text)
        self.float9.value = float(uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text)
        # ---------  mechanics 
        self.float10.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text)
        self.float11.value = float(uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text)
        self.bool0.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'].lower()))
        self.bool1.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'].lower()))
        # ---------  motility 
        self.float14.value = float(uep.find('.//cell_definition[1]//phenotype//motility//speed').text)
        self.float15.value = float(uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text)
        self.float16.value = float(uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text)
        self.bool2.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text.lower()))
        self.bool3.value = ('true' == (uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text.lower()))
        # ---------  intracellular
        self.bnd_filenames[0].value = uep.find('.//cell_definition[1]//phenotype//intracellular//bnd_filename').text
        self.cfg_filenames[0].value = uep.find('.//cell_definition[1]//phenotype//intracellular//cfg_filename').text
        self.float17.value = float(uep.find('.//cell_definition[1]//phenotype//intracellular//time_step').text)

        init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')

        for value in init_values:
            if value.get('node') == 'GF':
                self.bool4.value = True
                self.float18.value = float(value.text)
            elif value.get('node') == 'ECM':
                self.bool5.value = True
                self.float19.value = float(value.text)
            elif value.get('node') == 'Oxy':
                self.bool6.value = True
                self.float20.value = float(value.text)
            elif value.get('node') == 'Neigh':
                self.bool7.value = True
                self.float21.value = float(value.text)
            elif value.get('node') == 'TGFbeta':
                self.bool8.value = True
                self.float22.value = float(value.text)
            elif value.get('node') == 'DNAdamage':
                self.bool9.value = True
                self.float23.value = float(value.text)

        ##### MUTATIONS

        mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')

        for mutation in mutations:
            if mutation.get('node') == 'CTNNB1':
                self.bool10.value = True
                self.float24.value = float(value.text)
            elif mutation.get('node') == 'p53':
                self.bool11.value = True
                self.float25.value = float(value.text)
            elif mutation.get('node') == 'p63':
                self.bool12.value = True
                self.float26.value = float(value.text)
            elif mutation.get('node') == 'p73':
                self.bool14.value = True
                self.float28.value = float(value.text)
            elif mutation.get('node') == 'AKT1':
                self.bool16.value = True
                self.float30.value = float(value.text)
            elif mutation.get('node') == 'MMPs':
                self.bool13.value = True
                self.float27.value = float(value.text)
            elif mutation.get('node') == 'miR34':
                self.bool15.value = True
                self.float29.value = float(value.text)
            elif mutation.get('node') == 'ERK':
                self.bool17.value = True
                self.float31.value = float(value.text)
            elif mutation.get('node') == 'miR200':
                self.bool18.value = True
                self.float32.value = float(value.text)
            elif mutation.get('node') == 'miR203':
                self.bool19.value = True
                self.float33.value = float(value.text)


        # to add custom data  self.float32.value = float(uep.find('.//cell_definition[1]//phenotype//customdata//pintegrin').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//cell_definitions')  # find unique entry point

        # ------------------ cell_definition: default
        # ---------  cycle (advanced_Ki67_cycle_model)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[1]').text = str(self.float0.value)
        uep.find('.//cell_definition[1]//phenotype//cycle//phase_transition_rates//rate[2]').text = str(self.float1.value)
        # ---------  death 
        uep.find('.//cell_definition[1]//phenotype//death//model[1]//death_rate').text = str(self.float2.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//death_rate').text = str(self.float3.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//unlysed_fluid_change_rate').text = str(self.float4.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//lysed_fluid_change_rate').text = str(self.float5.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//cytoplasmic_biomass_change_rate').text = str(self.float6.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//nuclear_biomass_change_rate').text = str(self.float7.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//calcification_rate').text = str(self.float8.value)
        uep.find('.//cell_definition[1]//phenotype//death//model[2]//parameters//relative_rupture_volume').text = str(self.float9.value)
        # ---------  mechanics 
        uep.find('.//cell_definition[1]//phenotype//mechanics//cell_cell_repulsion_strength').text = str(self.float10.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//relative_maximum_adhesion_distance').text = str(self.float11.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_relative_equilibrium_distance').attrib['enabled'] = str(self.bool0.value)
        uep.find('.//cell_definition[1]//phenotype//mechanics//options//set_absolute_equilibrium_distance').attrib['enabled'] = str(self.bool1.value)
        # ---------  motility 
        uep.find('.//cell_definition[1]//phenotype//motility//speed').text = str(self.float14.value)
        uep.find('.//cell_definition[1]//phenotype//motility//persistence_time').text = str(self.float15.value)
        uep.find('.//cell_definition[1]//phenotype//motility//migration_bias').text = str(self.float16.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//enabled').text = str(self.bool2.value)
        uep.find('.//cell_definition[1]//phenotype//motility//options//use_2D').text = str(self.bool3.value)
        # ---------  intracellular
        uep.find('.//cell_definition[1]//phenotype//intracellular//bnd_filename').text = str(self.bnd_filenames[0].value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//cfg_filename').text = str(self.cfg_filenames[0].value)
        uep.find('.//cell_definition[1]//phenotype//intracellular//time_step').text = str(self.float17.value)

        #INITIAL VALUES

        if self.bool4.value == True:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            ET.SubElement(init_values, "initial_value", node="GF").text = str(self.float18.value)
        else:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            for value in init_values:
                if value.get('node') == 'GF':
                    #print('found optoSRC !')
                    init_values.remove(value)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')


        if self.bool5.value == True:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            ET.SubElement(init_values, "initial_value", node="ECM").text = str(self.float19.value)
        else:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            for value in init_values:
                if value.get('node') == 'ECM':
                    #print('found optoSRC !')
                    init_values.remove(value)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool6.value == True:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            ET.SubElement(init_values, "initial_value", node="Oxy").text = str(self.float20.value)
        else:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            for value in init_values:
                if value.get('node') == 'Oxy':
                    #print('found optoSRC !')
                    init_values.remove(value)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool7.value == True:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            ET.SubElement(init_values, "initial_value", node="Neigh").text = str(self.float21.value)
        else:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            for value in init_values:
                if value.get('node') == 'Neigh':
                    #print('found optoSRC !')
                    init_values.remove(value)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool8.value == True:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            ET.SubElement(init_values, "initial_value", node="TGFbeta").text = str(self.float22.value)
        else:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            for value in init_values:
                if value.get('node') == 'TGFbeta':
                    #print('found optoSRC !')
                    init_values.remove(value)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool9.value == True:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            ET.SubElement(init_values, "initial_value", node="DNAdamage").text = str(self.float23.value)
        else:
            init_values = uep.find('.//cell_definition[1]//phenotype//intracellular//initial_values')
            for value in init_values:
                if value.get('node') == 'DNAdamage':
                    #print('found optoSRC !')
                    init_values.remove(value)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        #MUTATIONS

        if self.bool10.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="CTNNB1").text = str(self.float24.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'CTNNB1':
                    #print('found DNAdamage !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no DNAdamage!')


        if self.bool11.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="p53").text = str(self.float25.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'p53':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool12.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="p63").text = str(self.float26.value)
        else:
            #print('Noooo!')
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'p63':
                    #print('found p63 !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no p63!')


        if self.bool13.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="MMPs").text = str(self.float27.value)
        else:
            #print('Noooo!')
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'MMPs':
                    #print('found MMPs !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no MMPs!')

        if self.bool14.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="p73").text = str(self.float28.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'p73':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool15.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="miR34").text = str(self.float29.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'miR34':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool16.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="AKT1").text = str(self.float30.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'AKT1':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool17.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="ERK").text = str(self.float31.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'ERK':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool18.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="miR200").text = str(self.float32.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'miR200':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')

        if self.bool19.value == True:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            ET.SubElement(mutations, "mutation", node="miR203").text = str(self.float33.value)
        else:
            mutations = uep.find('.//cell_definition[1]//phenotype//intracellular//mutations')
            for mutation in mutations:
                if mutation.get('node') == 'miR203':
                    #print('found optoSRC !')
                    mutations.remove(mutation)
                    break
                else:
                    continue
                    #print('there is no optoSRC!')
