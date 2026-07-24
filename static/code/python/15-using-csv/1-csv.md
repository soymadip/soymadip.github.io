CSV (Comma-Separated Values) is a lightweight file format used to store tabular data in plain text, designed for easy data exchange between programs, particularly spreadsheets and databases.

It is often used for moving data between programs with incompatible or proprietary formats.

While RFC 4180 provides a standard for the format, in practice, the term "CSV" is often used more broadly to refer to any text file that:

- Can be interpreted as tabular data
- Uses a delimiter to separate fields (columns)
- Uses line breaks to separate records (rows)
- Optionally includes a header in the first row

```csv
Data, Comment
100, Interpreted as a number (integer)
100.00, Interpreted as a number (floating-point)
2024-12-03, Interpreted as a date or a string (depending on the parser)
Hello World, Interpreted as text (string)
"1234", Interpreted as text instead of a number
```
