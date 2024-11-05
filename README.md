# Brief description of scripts

## addAuthorToPDF
As described. Adds authorship to your pdf files. Modify script to add other metadata to your pdf.

```python
python addauthortopdf.py
```
Enter a partial filename to search for relevant pdfs, before entering the full filename.

Enter your author's name, and that's it.

## generate_bestfit_circle
As described. Based on 10 points, generate the best fit circle. Displays results in a plot. Best fit circle eqn provided too!

- Calculates geometric distance of points from centre

- Calculates how much given points deviates from mean distance (i.e. residuals) 

- Uses least squares method to minimize the residuals to find best fit circle's centre. 

- Radius is then found from the mean of data points optimised by least squares method.

- Equation of circle is now derived with radius and coords of centre found

```python
python generate_bestfit_circle.py
```

## generate_bestfit_polynomial_line
As described. Based on 10 points, generate the best fit line. Displays results in a plot. Best fit polynomial eqn provided too!

```python
python generate_bestfit_polynomial_line.py
```
## pdfextractor
Parses through all PDFs for specific texts, saving them in a .csv file called output.csv. This file will be found in the same directory as the script itself.

**Requirements:** 

* Python >= 3.9.0
* Install pymupdf:
```
pip install pymupdf
```
* Script must be in the folder containing the folder containing the PDFs. 

```python
python pdfextractor.pdf
```
