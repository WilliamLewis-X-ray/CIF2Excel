"""
A list of datanames that are excluded from the excel file initial tabulation.
Loops are included as they will be manually dealt with.
Also has list which represent the order of data items.
"""

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

loop2a = """loop_  
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

loop5a = """loop_
  _exptl_crystal_face_index_h
  _exptl_crystal_face_index_k
  _exptl_crystal_face_index_l
  _exptl_crystal_face_perp_dist
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





exclusion_list = [
    '_refine_special_details',
    '_audit_creation_method',
    '_shelx_res_file',
    '_shelx_res_checksum',
    '_shelx_hkl_file',
    '_shelx_hkl_checksum',
    '_iucr_refine_instructions_details',
    '_shelx_fab_checksum',
    '_shelx_fab_file',
    loop1,
    '_publ_contact_author_address',
    '_publ_contact_author_email',
    '_publ_contact_author_id_orcid',
    '_publ_contact_author_name',
    '_publ_contact_author_phone',
    '_publ_section_references',
    loop2,
    loop2a,
    '_shelx_space_group_comment',
    loop3,
    loop4,
    loop5,
    loop5a,
    '_diffrn_measurement_details',
    '_reflns_special_details',
    '_olex2_refinement_description',
    loop_angle,
    loop_aniso,
    '_geom_special_details',
    loop_atom_site,
    loop_bond,
    loop_data,
    loop_hbond,
    loop_tors,
    'data_'
    ]

#next list is order in the excel spreadsheet. 
#Anything not in it gets appended to it.

spreadsheet_order = [
    '_cell_length_a',
    '_cell_length_b',
    '_cell_length_c',
    '_cell_angle_alpha',
    '_cell_angle_beta',
    '_cell_angle_gamma',
    '_cell_volume',
    '_space_group_crystal_system',
    '_space_group_IT_number',
    '_space_group_name_H-M_alt',
    '_space_group_name_Hall',
    '_diffrn_ambient_temperature',
    '_cell_measurement_temperature',
    '_diffrn_reflns_av_R_equivalents',
    '_diffrn_reflns_av_unetI/netI',
    '_diffrn_measured_fraction_theta_full',
    '_diffrn_reflns_theta_full',
    '_diffrn_radiation_wavelength',
    '_reflns_number_gt',
    '_reflns_number_total',
    '_diffrn_reflns_number',
    '_refine_ls_R_factor_gt',
    '_refine_ls_wR_factor_ref',
    '_refine_ls_restrained_S_all',
    '_refine_diff_density_max',
    '_refine_diff_density_min',
    '_refine_diff_density_rms',
    '_refine_ls_number_reflns',
    '_refine_ls_number_parameters',
    '_refine_ls_number_restraints',
    '_refine_ls_shift/su_max',
    '_exptl_crystal_colour',
    '_exptl_crystal_density_diffrn',
    '_exptl_crystal_description',
    '_exptl_crystal_F_000',
    '_exptl_crystal_size_max',
    '_exptl_crystal_size_mid',
    '_exptl_crystal_size_min',
    '_chemical_formula_sum',
    '_chemical_formula_weight',
    '_cell_formula_units_Z',
    '_exptl_absorpt_coefficient_mu',
    '_exptl_absorpt_correction_T_max',
    '_exptl_absorpt_correction_T_min',
    '_exptl_absorpt_correction_type',
    ]
