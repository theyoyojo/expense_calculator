from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint
from IPython import embed

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

TEST_SHEET_ID = '1WV6Gkywyd3MOI6fmWbAwGH7fo2ozSFQLTFpkqJQ4Qxo'
SECRET_API_KEY = 'LMAO_DONT_COMMIT_SECRET_KEYS'


def get_values_from_public_sheet(sheetId,apiKey):
    return build('sheets','v4',developerKey=apiKey) \
            .spreadsheets() \
            .get( \
                spreadsheetId=sheetId, \
                includeGridData=True, \
                fields='sheets/data/rowData/values/formattedValue') \
                .execute()

def get_string_from_document(document,rowIndex,columnIndex):
    return document['sheets'][0]['data'][0] \
            ['rowData'][rowIndex]['values'][columnIndex]['formattedValue']

# Only accepts single digits, sry bud
def get_indexes_from_cell_reference(row,column):
    return (row - 1,ord(column) - ord('A'))

def get_string_from_document_cell_reference(document,rowNumber,columnLetter):
    rowColumnIndexTuple = get_indexes_from_cell_reference(rowNumber,columnLetter)
    return get_string_from_document(document,
            rowColumnIndexTuple[0],rowColumnIndexTuple[1])


def main():
    document = get_values_from_public_sheet(TEST_SHEET_ID,SECRET_API_KEY)
    row2col2 = get_string_from_document_cell_reference(document,2,'B')

    #embed()


    print("Value in 2B is: %s" % row2col2)


if __name__ == '__main__':
    main()
