from src.data.dto import FileInfo

class HtmlOutput:

    def html_output_file(files: list) -> None:
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Log Files Analisys Service</title>
            <style>
                header {{
                    background-color: #dddddd;
                    color: #333;
                    padding: 10px;
                    text-align: center;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%
                }}
                th, td {{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }}
                th {{
                    background-color: #f2f2f2;
                    cursor: pointer;
                }}
                th:hover {{
                    background-color: #e0e0e0;
                }}
            </style>
        </head>
        <body>
            <header>
                <h1>Result</h1>
            </header>
            <table id="sortable-table">
                <thead>
                    <tr>
                        <th onclick="sortTable(0)">FileName</th>
                        <th onclick="sortTable(1)">LogRecords</th>
                        <th onclick="sortTable(2)">LogErrors</th>
                        <th onclick="sortTable(3)">FirstErrorDate</th>
                        <th onclick="sortTable(4)">LastErrorDate</th>
                    </tr>
                </thead>
                <tbody>
                    {"".join([f"<tr><td>{file.name}</td><td>{file.log_records}</td><td>{file.log_errors}</td><td>{file.first_error_date}</td><td>{file.last_error_date}</td></tr>" for file in files])}
                </tbody>
            </table>
            
            <script>
                var sortingStates = new Array(5).fill(true);

                function sortTable(columnIndex) {{
                    var table, rows, switching, i, x, y, shouldSwitch;
                    table = document.getElementById("sortable-table");
                    switching = true;
                    while (switching) {{
                        switching = false;
                        rows = table.getElementsByTagName("tr");
                        for (i = 1; i < (rows.length - 1); i++) {{
                            shouldSwitch = false;
                            x = rows[i].getElementsByTagName("td")[columnIndex];
                            y = rows[i + 1].getElementsByTagName("td")[columnIndex];
                            var xValue = x.innerHTML.toLowerCase();
                            var yValue = y.innerHTML.toLowerCase();
                            if (sortingStates[columnIndex]) {{
                                if (xValue > yValue) {{
                                    shouldSwitch = true;
                                    break;
                                }}
                            }} else {{
                                if (xValue < yValue) {{
                                    shouldSwitch = true;
                                    break;
                                }}
                            }}
                        }}
                        if (shouldSwitch) {{
                            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                            switching = true;
                        }}
                    }}
                    sortingStates[columnIndex] = !sortingStates[columnIndex];
                }}
            </script>
        </body>
        </html>                
        """

        with open("sortable_table.html", "w") as html_file:
            html_file.write(html_template)
            print('HTML file was created!')