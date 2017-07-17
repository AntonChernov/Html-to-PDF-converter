import pdfkit
import os

def test_pdf(type_of_data, filename, url=None):
    options = {
    'page-size': 'A4',
    'margin-top': '0.25in',
    'margin-right': '0.25in',
    'margin-bottom': '0.25in',
    'margin-left': '0.25in',
    }
    if type_of_data == '1':
        pdfkit.from_url('{0}'.format(url), str(os.getcwd()) + '/{0}.pdf'.format(filename), options=options)
    else:
        pdfkit.from_string('/********/b_text.html', '{0}.pdf'.format(filename))
        # pdfkit.from_file(css='/static/css/styles.css')


if __name__ == '__main__':
    type_of_data = input('Please input type(\n 1: for URL \n 2: for HTML file)\n Enter you choice: ')
    if type_of_data == '1':
        url = input('Please input url: ')
        filename = input('Please input filename: ')
        test_pdf(type_of_data, filename, url=url)
    else:
        filename = input('Please input filename: ')
        test_pdf(type_of_data, filename)
