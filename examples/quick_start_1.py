#!/usr/bin/env python3
"""
Quick start example 1 for the quetzal-annotator package.
"""

import quetzal_annotator

def main():
    # Define a Universal Spectrum Identifier for a spectrum deposited to ProteomeXchange
    usi_string = 'mzspec:PXD015223:QExHF06277:scan:4202:HAEEQPTM[Oxidation]PR/2'

    # Create a spectrum object and fetch a spectrum via a USI
    spectrum = quetzal_annotator.Spectrum()
    spectrum.fetch_spectrum(usi_string)

    # Parse the USI string into an object and parse the peptidoform part
    usi = quetzal_annotator.UniversalSpectrumIdentifier(usi_string)
    peptidoform = quetzal_annotator.ProformaPeptidoform(usi.peptidoform_string)

    # Annotate the spectrum
    annotator = quetzal_annotator.SpectrumAnnotator()
    annotator.annotate(spectrum, peptidoforms=[peptidoform], charges=[usi.charge])

    # Display the results
    print(f"Spectrum USI: {usi_string}")
    print(spectrum.show())

    return spectrum

if __name__ == "__main__":
    main() 