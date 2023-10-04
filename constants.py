sql_query = """
SELECT t.*, c.SYMBOL, tl.TRANSACTION_ID , tl.SUBSIDIARY_ID, tl.AMOUNT, tl.AMOUNT_FOREIGN, s.NAME
FROM dea.netsuite.TRANSACTIONS t
JOIN dea.netsuite.CURRENCIES c ON t.CURRENCY_ID = c.CURRENCY_ID
JOIN dea.netsuite.TRANSACTION_LINES tl ON t.TRANSACTION_ID = tl.TRANSACTION_ID
JOIN dea.netsuite.SUBSIDIARIES s ON tl.SUBSIDIARY_ID = s.SUBSIDIARY_ID
WHERE tl.AMOUNT >= 0;
"""

connectionUser = 'Driver=ODBC Driver 17 for SQL Server;' \
                 'Server=testdb.bi.aws.intellij.net;' \
                 'Database=dea;' \
                 'uid=tomas_benko;pwd=q&)x5#^MF8d-4}DdN5DMpz!fZf81XD;'

output_path = 'C:/Users/tbenko/PycharmProjects/JB1/output.xlsx'

settlements_path = 'C:/Users/tbenko/PycharmProjects/JB1/jb-dea-test-assignment/settlement/'


