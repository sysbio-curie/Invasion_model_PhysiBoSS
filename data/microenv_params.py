 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class MicroenvTab(object):

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


        menv_var1 = Button(description='oxygen (mmHg)', disabled=True, layout=name_button_layout)
        menv_var1.style.button_color = 'tan'

        param_name1 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.oxygen_diffusion_coefficient = FloatText(value=6000.0,
          step=100,style=style, layout=widget_layout)

        param_name2 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.oxygen_decay_rate = FloatText(value=.1,
          step=0.01,style=style, layout=widget_layout)
        param_name3 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.oxygen_initial_condition = FloatText(value=38.0,style=style, layout=widget_layout)
        param_name4 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.oxygen_Dirichlet_boundary_condition = FloatText(value=38.0,style=style, layout=widget_layout)
        self.oxygen_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var2 = Button(description='ecm', disabled=True, layout=name_button_layout)
        menv_var2.style.button_color = 'lightgreen'

        param_name5 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.ecm_diffusion_coefficient = FloatText(value=1e-85,
          step=1e-86,style=style, layout=widget_layout)

        param_name6 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.ecm_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name7 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.ecm_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name8 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.ecm_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.ecm_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var3 = Button(description='TGFbeta', disabled=True, layout=name_button_layout)
        menv_var3.style.button_color = 'tan'

        param_name9 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.TGFbeta_diffusion_coefficient = FloatText(value=1e-85,
          step=1e-86,style=style, layout=widget_layout)

        param_name10 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.TGFbeta_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name11 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.TGFbeta_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name12 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.TGFbeta_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.TGFbeta_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)

        menv_var4 = Button(description='light', disabled=True, layout=name_button_layout)
        menv_var4.style.button_color = 'lightgreen'

        param_name13 = Button(description='diffusion_coefficient', disabled=True, layout=name_button_layout)

        self.light_diffusion_coefficient = FloatText(value=1e-85,
          step=1e-86,style=style, layout=widget_layout)

        param_name14 = Button(description='decay_rate', disabled=True, layout=name_button_layout)

        self.light_decay_rate = FloatText(value=0,
          step=0.01,style=style, layout=widget_layout)
        param_name15 = Button(description='initial_condition', disabled=True, layout=name_button_layout)

        self.light_initial_condition = FloatText(value=0,style=style, layout=widget_layout)
        param_name16 = Button(description='Dirichlet_boundary_condition', disabled=True, layout=name_button_layout)

        self.light_Dirichlet_boundary_condition = FloatText(value=0,style=style, layout=widget_layout)
        self.light_Dirichlet_boundary_condition_toggle = Checkbox(description='on/off', disabled=False,style=style, layout=widget_layout)
        self.calculate_gradient = Checkbox(description='calculate_gradients', disabled=False, layout=desc_button_layout)
        self.track_internal = Checkbox(description='track_in_agents', disabled=False, layout=desc_button_layout)


         #  ------- micronenv info
        menv_units_button1 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button2 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button3 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button4 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button5 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button7 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button8 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button9 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button10 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button11 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button12 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button13 = Button(description='micron^2/min', disabled=True, layout=units_button_layout) 
        menv_units_button14 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        menv_units_button15 = Button(description='mmHg', disabled=True, layout=units_button_layout) 
        menv_units_button16 = Button(description='mmHg', disabled=True, layout=units_button_layout) 




        row_oxygen = [menv_var1,  ] 
        row1 = [param_name1, self.oxygen_diffusion_coefficient, menv_units_button1]
        row2 = [param_name2, self.oxygen_decay_rate, menv_units_button2]
        row3 = [param_name3, self.oxygen_initial_condition, menv_units_button3]
        row4 = [param_name4, self.oxygen_Dirichlet_boundary_condition, menv_units_button4, self.oxygen_Dirichlet_boundary_condition_toggle]
        row_ecm = [menv_var2,  ] 
        row5 = [param_name5, self.ecm_diffusion_coefficient, menv_units_button5]
        row6 = [param_name6, self.ecm_decay_rate, menv_units_button6]
        row7 = [param_name7, self.ecm_initial_condition, menv_units_button7]
        row8 = [param_name8, self.ecm_Dirichlet_boundary_condition, menv_units_button8, self.ecm_Dirichlet_boundary_condition_toggle]
        row_TGFbeta = [menv_var3,  ] 
        row9 = [param_name9, self.TGFbeta_diffusion_coefficient, menv_units_button9]
        row10 = [param_name10, self.TGFbeta_decay_rate, menv_units_button10]
        row11 = [param_name11, self.TGFbeta_initial_condition, menv_units_button11]
        row12 = [param_name12, self.TGFbeta_Dirichlet_boundary_condition, menv_units_button12, self.TGFbeta_Dirichlet_boundary_condition_toggle]
        row_light = [menv_var4,  ] 
        row13 = [param_name13, self.light_diffusion_coefficient, menv_units_button13]
        row14 = [param_name14, self.light_decay_rate, menv_units_button14]
        row15 = [param_name15, self.light_initial_condition, menv_units_button15]
        row16 = [param_name16, self.light_Dirichlet_boundary_condition, menv_units_button16, self.light_Dirichlet_boundary_condition_toggle]
        row17 = [self.calculate_gradient,]
        row18 = [self.track_internal,]


        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box_oxygen = Box(children=row_oxygen, layout=box_layout)
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box_ecm = Box(children=row_ecm, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box_TGFbeta = Box(children=row_TGFbeta, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box_light = Box(children=row_light, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)

        self.tab = VBox([
          box_oxygen,
          box1,
          box2,
          box3,
          box4,
          box_ecm,
          box5,
          box6,
          box7,
          box8,
          box_TGFbeta,
          box9,
          box10,
          box11,
          box12,
          box_light,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point

        self.oxygen_diffusion_coefficient.value = float(vp[0].find('.//diffusion_coefficient').text)
        self.oxygen_decay_rate.value = float(vp[0].find('.//decay_rate').text)
        self.oxygen_initial_condition.value = float(vp[0].find('.//initial_condition').text)
        self.oxygen_Dirichlet_boundary_condition.value = float(vp[0].find('.//Dirichlet_boundary_condition').text)
        if vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.oxygen_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.oxygen_Dirichlet_boundary_condition_toggle.value = False

        self.ecm_diffusion_coefficient.value = float(vp[1].find('.//diffusion_coefficient').text)
        self.ecm_decay_rate.value = float(vp[1].find('.//decay_rate').text)
        self.ecm_initial_condition.value = float(vp[1].find('.//initial_condition').text)
        self.ecm_Dirichlet_boundary_condition.value = float(vp[1].find('.//Dirichlet_boundary_condition').text)
        if vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.ecm_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.ecm_Dirichlet_boundary_condition_toggle.value = False

        self.TGFbeta_diffusion_coefficient.value = float(vp[2].find('.//diffusion_coefficient').text)
        self.TGFbeta_decay_rate.value = float(vp[2].find('.//decay_rate').text)
        self.TGFbeta_initial_condition.value = float(vp[2].find('.//initial_condition').text)
        self.TGFbeta_Dirichlet_boundary_condition.value = float(vp[2].find('.//Dirichlet_boundary_condition').text)
        if vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.TGFbeta_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.TGFbeta_Dirichlet_boundary_condition_toggle.value = False

        self.light_diffusion_coefficient.value = float(vp[3].find('.//diffusion_coefficient').text)
        self.light_decay_rate.value = float(vp[3].find('.//decay_rate').text)
        self.light_initial_condition.value = float(vp[3].find('.//initial_condition').text)
        self.light_Dirichlet_boundary_condition.value = float(vp[3].find('.//Dirichlet_boundary_condition').text)
        if vp[3].find('.//Dirichlet_boundary_condition').attrib['enabled'].lower() == 'true':
          self.light_Dirichlet_boundary_condition_toggle.value = True
        else:
          self.light_Dirichlet_boundary_condition_toggle.value = False

        if uep.find('.//options//calculate_gradients').text.lower() == 'true':
          self.calculate_gradient.value = True
        else:
          self.calculate_gradient.value = False
        if uep.find('.//options//track_internalized_substrates_in_each_agent').text.lower() == 'true':
          self.track_internal.value = True
        else:
          self.track_internal.value = False
        


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp[0].find('.//diffusion_coefficient').text = str(self.oxygen_diffusion_coefficient.value)
        vp[0].find('.//decay_rate').text = str(self.oxygen_decay_rate.value)
        vp[0].find('.//initial_condition').text = str(self.oxygen_initial_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').text = str(self.oxygen_Dirichlet_boundary_condition.value)
        vp[0].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.oxygen_Dirichlet_boundary_condition_toggle.value).lower()

        vp[1].find('.//diffusion_coefficient').text = str(self.ecm_diffusion_coefficient.value)
        vp[1].find('.//decay_rate').text = str(self.ecm_decay_rate.value)
        vp[1].find('.//initial_condition').text = str(self.ecm_initial_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').text = str(self.ecm_Dirichlet_boundary_condition.value)
        vp[1].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.ecm_Dirichlet_boundary_condition_toggle.value).lower()

        vp[2].find('.//diffusion_coefficient').text = str(self.TGFbeta_diffusion_coefficient.value)
        vp[2].find('.//decay_rate').text = str(self.TGFbeta_decay_rate.value)
        vp[2].find('.//initial_condition').text = str(self.TGFbeta_initial_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').text = str(self.TGFbeta_Dirichlet_boundary_condition.value)
        vp[2].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.TGFbeta_Dirichlet_boundary_condition_toggle.value).lower()

        vp[3].find('.//diffusion_coefficient').text = str(self.light_diffusion_coefficient.value)
        vp[3].find('.//decay_rate').text = str(self.light_decay_rate.value)
        vp[3].find('.//initial_condition').text = str(self.light_initial_condition.value)
        vp[3].find('.//Dirichlet_boundary_condition').text = str(self.light_Dirichlet_boundary_condition.value)
        vp[3].find('.//Dirichlet_boundary_condition').attrib['enabled'] = str(self.light_Dirichlet_boundary_condition_toggle.value).lower()


        uep.find('.//options//calculate_gradients').text = str(self.calculate_gradient.value)
        uep.find('.//options//track_internalized_substrates_in_each_agent').text = str(self.track_internal.value)
