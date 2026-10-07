// -------------------------
// LOAD DATA INFORMATION
// -------------------------

async function loadInfo() {

    const response = await fetch("/info");

    const data = await response.json();

    document.getElementById("rows").innerText =
        data.rows;

    document.getElementById("columns").innerText =
        data.columns;

    document.getElementById("missing").innerText =
        data.missing_values;

    document.getElementById("duplicates").innerText =
        data.duplicates;
}


// -------------------------
// SEARCH
// -------------------------

async function searchData() {

    const column =
        document.getElementById("searchColumn").value;

    const value =
        document.getElementById("searchValue").value;


    const response = await fetch("/search", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            column: column,
            value: value
        })

    });


    const data = await response.json();

    console.log(data);

    if (data.success) {

        alert(
            "Found " +
            data.data.length +
            " matching records."
        );

        console.log(data.data);

    } else {

        alert(data.message);

    }

}


// -------------------------
// CALCULATE
// -------------------------

async function calculate() {

    const operation =
        document.getElementById("operation").value;

    const column =
        document.getElementById("calcColumn").value;


    const response = await fetch("/calculate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            operation: operation,
            column: column

        })

    });


    const data = await response.json();


    if (data.success) {

        document.getElementById("result").innerText =
            "Result: " + data.result;

    } else {

        alert(data.message);

    }

}


// Start application

loadInfo();

// -------------------------
// AI AGENT
// -------------------------

async function sendCommand() {

    const command =
        document.getElementById("commandInput").value;


    if (!command.trim()) {

        alert("Please enter a command.");

        return;
    }


    const resultBox =
        document.getElementById("agentResult");


    resultBox.innerText =
        "🤖 Agent is thinking...";


    const response = await fetch("/command", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            command: command
        })

    });


    const data = await response.json();


    if (!data.success) {

        resultBox.innerText =
            "❌ " + data.message;

        return;
    }


    resultBox.innerText =
        "✅ " + data.message;


    // Display table results

    if (data.type === "table" && data.data) {

        console.log(data.data);

        let table = "<table>";

        const columns =
            Object.keys(data.data[0]);


        table += "<tr>";

        columns.forEach(column => {

            table += `<th>${column}</th>`;

        });

        table += "</tr>";


        data.data.forEach(row => {

            table += "<tr>";

            columns.forEach(column => {

                table += `<td>${row[column]}</td>`;

            });

            table += "</tr>";

        });


        table += "</table>";


        resultBox.innerHTML =
            "✅ " + data.message + "<br><br>" + table;

    }

}


// -------------------------
// EXAMPLE COMMAND
// -------------------------

function useCommand(command) {

    document.getElementById("commandInput").value =
        command;

}