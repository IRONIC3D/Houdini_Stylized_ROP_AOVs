########################################################################
# Authored by Iyad Horani.
# Published under the Creative Commons Attribution 3.0 License.
# Some Rights Reserved <http://creativecommons.org/licenses/by/3.0/>.
#
# This script enables the default AOVs required by Stylized Looks.
# Select the RenderMan ROP and run the script to enable the AOVs. 
#
########################################################################

import hou

def toggle_parameters(node, parameters_to_toggle, enable=True):
    for parm_name in parameters_to_toggle:
        parm = node.parm(parm_name)
        if parm is not None:
            parm.set(1 if enable else 0)  # Toggle on/off based on 'enable'
        else:
            hou.ui.displayMessage(f"Parameter '{parm_name}' not found on the node.", severity=hou.severityType.Error)

# Get the currently selected node(s)
selected_nodes = hou.selectedNodes()

if selected_nodes:
    node = selected_nodes[0] 
    parameters_to_toggle = [
        "ri_quickaov_Nn_0",
        "ri_quickaov_P_0",
        "ri_quickaov_sampleCount_0",
        "ri_quickaov_albedo_0",
        "ri_quickaov_directDiffuse_0",
        "ri_quickaov_directSpecular_0",
        "ri_quickaov_NPRlineOut_0",
        "ri_quickaov_NPRcurvature_0",
        "ri_quickaov_NPRoutline_0",
        "ri_quickaov_NPRlineNZ_0",
        "ri_quickaov_NPRsections_0",
        "ri_quickaov_NPRlineCamdist_0",
        "ri_quickaov_NPRmask_0",
        "ri_quickaov_NPRlineAlbedo_0",
        "ri_quickaov_NPRlineWidth_0",
        "ri_quickaov_NPRlineOutAlpha_0",
        "ri_quickaov_NPRtextureCoords_0",
        "ri_quickaov_NPRtoonDiff_0",
        "ri_quickaov_NPRtoonOut_0",
        "ri_quickaov_NPRhatchOut_0",
        "ri_quickaov_NPRPtriplanar_0",
        "ri_quickaov_NPRNtriplanar_0",
        "ri_quickaov_NPRdistort_0",
        "ri_quickaov_NPRalbedo_0"
    ]

    toggle_parameters(node, parameters_to_toggle)
else:
    hou.ui.displayMessage("Please select a node.", severity=hou.severityType.Warning)