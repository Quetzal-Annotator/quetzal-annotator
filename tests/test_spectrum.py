import pytest
import sys
import json

sys.path.append("../quetzal-annotator")
from spectrum import Spectrum



def test_init_without_params():
    spectrum = Spectrum()
    assert '1' in spectrum.analytes
    assert len(spectrum.peak_list) == 0



def test_init_with_3params():
    attributes = [ { 'accession': 'MS:1000041', 'name': 'charge state', 'value': 2 } ]
    mzs = [ 100.0, 200.0 ]
    intensities = [ 500.0, 600.0 ]
    spectrum = Spectrum( attributes, mzs, intensities)
    assert len(spectrum.peak_list) == 2



def test_MGF_import():
    mgf_spectrum = '''BEGIN IONS
TITLE=Spectrum 1
PRECURSOR=418.2175
PEPMASS=1251.63067059936
CHARGE=3+
COM=mzspec:PXD006201:20150913SL_Qe2_HEP2_UBISITE_rep3_BORT_HpH_5.mzML:scan:04132:SDGVSPK[UNIMOD:121]HVGR/3
COM=FTMS + p NSI d Full ms2 418.22@hcd28.00 [100.00-1300.00]
101.0714	1467.2856
102.0552	1873.2421
105.066   1440.8665
END IONS'''

    spectrum = Spectrum()
    proxi_spectrum = spectrum.convert_MGF_to_proxi_spectrum(mgf_spectrum)
    assert isinstance(proxi_spectrum, list)
    assert len(proxi_spectrum) == 1
    assert len(proxi_spectrum[0]['mzs']) == 3

    charge = None
    precursor_mz = None
    for attribute in proxi_spectrum[0]['attributes']:
        if attribute['accession'] == 'MS:1000041':
            charge = attribute['value']
        if attribute['accession'] == 'MS:1000744':
            precursor_mz = attribute['value']
    assert charge == 3
    assert precursor_mz == 418.2175



def test_fetch_spectrum():
    usi_string = 'mzspec:PXD005336:Varlitinib_01410_A01_P014203_B00_A00_R1:scan:19343:LLSILSR/2'

    spectrum = Spectrum()
    spectrum.fetch_spectrum(usi_string)

    assert len(spectrum.peak_list) == 33
    assert len(spectrum.attribute_list) == 9

    charge = None
    precursor_mz = None
    for attribute in spectrum.attribute_list:
        if attribute['accession'] == 'MS:1000041':
            charge = attribute['value']
        if attribute['accession'] == 'MS:1000744':
            precursor_mz = attribute['value']
    assert charge == '2'
    assert precursor_mz == '401.2628'

