function updateTable(data) {
    var table = document.getElementById('hostsTable');
    // Borra la tabla antes de agregar datos nuevos
    while(table.rows.length > 1) {
        table.deleteRow(1);
    }
    // Añade cada host a la tabla
    data.forEach(function(host) {
        var row = table.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        cell1.innerHTML = host.name;
        cell2.innerHTML = host.address;
        cell3.innerHTML = host.port;
    });
}

function fetchHosts() {
    fetch('http://localhost:5000/hosts')
        .then(response => response.json())
        .then(data => updateTable(data));
}

// Llama a fetchHosts cada 5 segundos para mantener la tabla actualizada
setInterval(fetchHosts, 5000);
