#!/usr/bin/env python3
"""
Quick start example 2 for the quetzal-annotator package.
"""

import quetzal_annotator

def main():
    # Start with manually defined spectrum data
    mzs = [102.0551, 129.1024, 147.1134, 175.1190, 204.1343, 227.1026, 518.7215, 727.1234, 810.3399]
    intensities = [12.3, 87.5, 45.2, 100.0, 78.9, 54.8, 12.6, 2.1, 96.3]
    precursor_mz = 1002.4567
    charge = 2
    proforma_string = 'PEPT[Phospho]IDER'

    # Create a spectrum object and fill it with data
    spectrum = quetzal_annotator.Spectrum()
    spectrum.fill(mzs=mzs, intensities=intensities, precursor_mz=precursor_mz, charge_state=charge)

    # Create a peptidoform object using ProForma notation
    peptidoform = quetzal_annotator.ProformaPeptidoform(proforma_string)

    # Annotate the spectrum
    annotator = quetzal_annotator.SpectrumAnnotator()
    annotator.annotate(spectrum, peptidoforms=[peptidoform], charges=[charge])

    # Display the results
    print(f"Spectrum annotated with {proforma_string} {charge}+")
    print(spectrum.show())

    return spectrum

if __name__ == "__main__":
    main() 