loop1 = """loop_
  _publ_author_name
  _publ_author_email
  _publ_author_address"""

loop2 = """loop_
  _atom_type_symbol
  _atom_type_description
  _atom_type_scat_dispersion_real
  _atom_type_scat_dispersion_imag
  _atom_type_scat_source"""

loop3 = """loop_
  _space_group_symop_operation_xyz"""

loop4 = """loop_
  _exptl_crystal_face_index_h
  _exptl_crystal_face_index_k
  _exptl_crystal_face_index_l
  _exptl_crystal_face_perp_dist"""

loop5 = """loop_
  _exptl_oxdiff_crystal_face_indexfrac_h
  _exptl_oxdiff_crystal_face_indexfrac_k
  _exptl_oxdiff_crystal_face_indexfrac_l
  _exptl_oxdiff_crystal_face_x
  _exptl_oxdiff_crystal_face_y
  _exptl_oxdiff_crystal_face_z"""

loop_atom_site = """loop_
  _atom_site_label
  _atom_site_type_symbol
  _atom_site_fract_x
  _atom_site_fract_y
  _atom_site_fract_z
  _atom_site_U_iso_or_equiv
  _atom_site_adp_type
  _atom_site_occupancy
  _atom_site_site_symmetry_order
  _atom_site_calc_flag
  _atom_site_refinement_flags_posn
  _atom_site_refinement_flags_adp
  _atom_site_refinement_flags_occupancy
  _atom_site_disorder_assembly
  _atom_site_disorder_group"""

loop_aniso = """loop_
  _atom_site_aniso_label
  _atom_site_aniso_U_11
  _atom_site_aniso_U_22
  _atom_site_aniso_U_33
  _atom_site_aniso_U_23
  _atom_site_aniso_U_13
  _atom_site_aniso_U_12"""

loop_bond = """loop_
  _geom_bond_atom_site_label_1
  _geom_bond_atom_site_label_2
  _geom_bond_distance
  _geom_bond_site_symmetry_2
  _geom_bond_publ_flag"""

loop_angle = """loop_
  _geom_angle_atom_site_label_1
  _geom_angle_atom_site_label_2
  _geom_angle_atom_site_label_3
  _geom_angle
  _geom_angle_site_symmetry_1
  _geom_angle_site_symmetry_3
  _geom_angle_publ_flag"""

loop_hbond = """loop_
  _geom_hbond_atom_site_label_D
  _geom_hbond_atom_site_label_H
  _geom_hbond_atom_site_label_A
  _geom_hbond_distance_DH
  _geom_hbond_distance_HA
  _geom_hbond_distance_DA
  _geom_hbond_angle_DHA
  _geom_hbond_site_symmetry_A"""

loop_tors = """loop_
  _geom_torsion_atom_site_label_1
  _geom_torsion_atom_site_label_2
  _geom_torsion_atom_site_label_3
  _geom_torsion_atom_site_label_4
  _geom_torsion
  _geom_torsion_site_symmetry_1
  _geom_torsion_site_symmetry_2
  _geom_torsion_site_symmetry_3
  _geom_torsion_site_symmetry_4
  _geom_torsion_publ_flag"""

loop_data = """loop_
  _refln_index_h
  _refln_index_k
  _refln_index_l
  _refln_F_squared_meas
  _refln_F_squared_sigma"""