# Tests wing segment member functions

import machupX as MX
import numpy as np
import json
import subprocess as sp

input_file = "test/input_for_testing.json"

def test_all_wing_segments_get_added():
    # Tests that all wing segments have been added and are available through 
    # both the tree and the dict.

    _,_,airplane_dict,_,_ = MX.helpers.parse_input(input_file)

    wing_segments = []
    wing_segment_sides = []
    for key in airplane_dict["wings"]:
        wing_segments.append(key)
        wing_segment_sides.append(airplane_dict["wings"][key]["side"])

    # Create scene
    scene = MX.Scene(input_file)

    # Check for each wing segment in both the tree and the dict
    wing_dict = scene._airplanes["test_plane"].wing_segments
    for segment_name, segment_side in zip(wing_segments, wing_segment_sides):

        if segment_side == "left" or segment_side == "both":
            name = segment_name+"_left"

            # Retrieve from dictionary
            dict_segment = wing_dict[name]

            # Retrieve from tree
            tree_segment = scene._airplanes["test_plane"]._get_wing_segment(name)

            # Make sure these reference the same object
            assert dict_segment is tree_segment

        if segment_side == "right" or segment_side == "both":
            name = segment_name+"_right"

            # Retrieve from dictionary
            dict_segment = wing_dict[name]

            # Retrieve from tree
            tree_segment = scene._airplanes["test_plane"]._get_wing_segment(name)

            # Make sure these reference the same object
            assert dict_segment is tree_segment