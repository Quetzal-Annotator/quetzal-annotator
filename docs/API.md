# Quetzal Annotator API Documentation

## Overview

The `quetzal-annotator` package provides comprehensive tools for annotating peptide fragment ion mass spectra using the PSI mzPAF standard. This document provides detailed API documentation for all major components.

## Installation

```bash
pip install quetzal-annotator
```

## Quick Start

```python
import numpy as np
from quetzal_annotator import Spectrum, SpectrumAnnotator, ProformaPeptidoform

# Create spectrum data
mzs = np.array([147.1134, 175.1190, 204.1343])
intensities = np.array([100.0, 45.2, 78.9])

# Create spectrum
spectrum = Spectrum(mzs=mzs, intensities=intensities)
spectrum.precursor_mz = 1002.4567
spectrum.charge = 2

# Create peptidoform
peptidoform = ProformaPeptidoform("PEPTIDE")

# Annotate
annotator = SpectrumAnnotator()
annotated_spectrum = annotator.annotate(spectrum, peptidoform)
```

## Core Classes

### Spectrum

The main class for representing mass spectrometry spectra.

```python
class Spectrum:
    def __init__(self, mzs: np.ndarray, intensities: np.ndarray, 
                 precursor_mz: float = None, charge: int = None)
```

**Parameters:**
- `mzs`: Array of m/z values (monotonically increasing)
- `intensities`: Array of intensity values
- `precursor_mz`: Precursor ion m/z value
- `charge`: Precursor ion charge state

**Attributes:**
- `mzs`: Array of m/z values
- `intensities`: Array of intensity values
- `precursor_mz`: Precursor ion m/z
- `charge`: Precursor ion charge
- `annotations`: List of peak annotations

### SpectrumAnnotator

Main class for annotating spectra with peptidoforms.

```python
class SpectrumAnnotator:
    def __init__(self, tolerance_ppm: float = 10.0)
    
    def annotate(self, spectrum: Spectrum, peptidoform: Peptidoform) -> Spectrum
```

**Parameters:**
- `tolerance_ppm`: Mass tolerance in parts per million for peak matching

**Methods:**
- `annotate()`: Annotates a spectrum with a peptidoform

### ProformaPeptidoform

Class for handling peptidoforms in ProForma notation.

```python
class ProformaPeptidoform:
    def __init__(self, sequence: str)
```

**Parameters:**
- `sequence`: ProForma sequence string

**Attributes:**
- `sequence`: The peptide sequence
- `mz`: Theoretical m/z value
- `mass`: Theoretical mass

### UniversalSpectrumIdentifier

Class for parsing and handling Universal Spectrum Identifiers (USI).

```python
class UniversalSpectrumIdentifier:
    def __init__(self, usi_string: str)
```

**Parameters:**
- `usi_string`: USI string to parse

**Attributes:**
- `dataset`: Dataset identifier
- `filename`: File name
- `scan`: Scan number
- `interpretation`: Peptide interpretation (if present)

### UniversalSpectrumIdentifierValidator

Class for validating USI strings.

```python
class UniversalSpectrumIdentifierValidator:
    def validate(self, usi: UniversalSpectrumIdentifier) -> bool
    def get_errors(self) -> List[str]
```

**Methods:**
- `validate()`: Returns True if USI is valid
- `get_errors()`: Returns list of validation errors

## Advanced Usage

### Spectrum Examination

```python
from quetzal_annotator import SpectrumExaminer

examiner = SpectrumExaminer()
results = examiner.examine(annotated_spectrum)
```

### Spectrum Comparison

```python
from quetzal_annotator import SpectrumComparator

comparator = SpectrumComparator()
similarity = comparator.compare(spectrum1, spectrum2)
```

### Ontology Handling

```python
from quetzal_annotator import Ontology, OntologyCollection

# Load PSI-MS ontology
ontology = Ontology("psi-ms.obo")
collection = OntologyCollection()
collection.add_ontology(ontology)
```

## Data Files

The package includes several important data files:

- `psi-ms.obo`: PSI-MS ontology in OBO format
- `psi-ms.json`: PSI-MS ontology in JSON format
- `unimod.obo`: UniMod modifications in OBO format
- `unimod.json`: UniMod modifications in JSON format

These files are automatically included in the package and can be accessed programmatically.

## Error Handling

The package provides comprehensive error handling:

```python
try:
    spectrum = Spectrum(mzs, intensities)
    annotated = annotator.annotate(spectrum, peptidoform)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Performance Considerations

- For large datasets, consider processing spectra in batches
- The annotation process is computationally intensive for complex peptidoforms
- USI validation is fast and can be used for real-time validation

## Contributing

Please refer to the main README for contribution guidelines and development setup instructions. 