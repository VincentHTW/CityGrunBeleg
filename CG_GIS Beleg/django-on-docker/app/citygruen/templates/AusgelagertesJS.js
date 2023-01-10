
// // Funktion für insert_pflanze.html, um an FileList zu kommen 

// let single = "Datei Ausgewählt";
// let multiple = "Datein Ausgewält";

// fileUploadStyling(single,multiple);

// function fileUploadStyling(single,multiple){
// let input = document.querySelectorAll("input[type=file]");
// for (let i = 0; i < input.length; i++) {
//     var inputFile = input[i];
//     inputFile.addEventListener('change',function(e){
//         console.log(this.files[0].name)
//         console.log(this.files)

//         var label = this.nextElementSibling;

//         if(this.files && this.files.length > 1){
//             label.innerHTML = this.files.length + ' ' + multiple;
//         }else{
//             label.innerHTML = this.files[0].name + ' ' + single;
//         }
//     });
// }
// }


// // HTML Form alter_pflanze

// {% include "include/nav.html" %}
// <h1 id="insert_head">Neue Pflanze anlegen</h1>
// <div class = "insert_form">
//     <form action="" method="post"  enctype="multipart/form-data">
//         {%  csrf_token %}
//         <div class = "form">
//             <label class = "insert_label"> <b>ID: </b></label>
//             <label class = "insert_label"> <b> {{ Pflanzen.first.id }}</b></label>
//         </div>

//         <div class = "form">
//             <label class = "insert_label"><b>Name: </b></label>
//             <label class = "insert_label"> <b> {{ Pflanzen.first.Name }}</b></label>
//         </div>

//         <div class = "form">
//             <label class = "insert_label"><b>Gattung: </b></label>
//             <label class = "insert_label"> <b> {{ Pflanzen.first.Gattung }}</b></label>
//         </div>

//         <div class = "form">
//             <label class = "insert_label" id="pflegehinweis"><b>Pflegehinweis: </b></label>
//             <label class = "insert_label"> <b> {{ Pflanzen.first.Pflegehinweis }}</b></label>
//         </div>

//         <div class = "form">
//                 <label class = "insert_label"><b>Bild: </b></label>
//                 <img src=" {{ Pflanzen.first.Picture }} " width="400" height="300">
//         </div>

//         <div class = "form">
//             <label class = "insert_label"><b>Status: </b></label>
//             <label class = "insert_label"> <b> {{ Pflanzen.first.Status }}</b></label>
//           </div>

//         <div class = "form">
//             <input type="submit" class = "insert_button" id="insert_submit" value="Absenden">
//             <input type="reset" class = "insert_button" id="insert_cancel" value="Zurücksetzen">
//         </div>

//         <script>
//             function getBase64(file) {
//                 var reader = new FileReader();
//                 reader.readAsDataURL(file);
//                 reader.onload = function () {
//                     console.log(reader.result);
//                     // In HTML anzeigen
//                     document.getElementById("insert_picure_label").value = reader.result; 
//                     document.getElementById("insert_picture_target").src = reader.result; 
//                     document.getElementById("insert_picture_target").style.display = 'inline';
//                 };
//                 reader.onerror = function (error) {
//                     console.log('Error: ', error);
//                 };
//             }

//             document.addEventListener("DOMContentLoaded", function(event) {  

//             document.getElementById('insert_picture').addEventListener('change', fileUploadStyling)

//             function fileUploadStyling() {
//                 let file = document.querySelector("input[type=file]").files[0];
//                 console.log(file);
//                 getBase64(file); // prints the base64 string
//             }
//             })
//         </script>

// Auswahlliste:
//                       {% if Pflanzen %}
//                     <div class="form">
//                         <label class = "insert_label"><b>Name eingeben: </b></label>
//                           <select name="top5" size="3">
//                             {% for Pflanze in Pflanzen %}
//                             <option> {{ Pflanzen.objects.get(id=1) }} </option>
//                             {% endfor %}
//                           </select>
//                     </div> 

//                        {% else %}
//                        <div class="container p-3 my-3 bg-dark text-white">No Data </div>
//                       {% endif %}

{/* <form action="" method="get"  enctype="multipart/form-data">
<div class = "form">
    <div class="Suche">
        {%  csrf_token %}
        <label class = "insert_label"> <b>Name eingeben: </b></label>
        <input class = "alter_input_Suche" type = "text" id="Suche_Standort" name = "Suche_Standort" value ="" placeholder="Name des Standortes eingeben" >
        <a href="{% url 'getID'%}"><button id="alter_suche_standort" class="alter_suche" >Suchen</button></a>
        
        {% if Standorte %}
        <label class = "insert_label"> <b>Standort auswählen: </b></label>
            <select name="Auswahlliste_Standort" size= {{ Standorte.count }}>
            {% for Standort in Standorte %}
                <option class="Auswahl_Standort" id="Auswahl_Standort">{{ Standort.id }} - {{ Standort.Name }} - {{ Standort.Adresse }}</option>
            {% endfor %}
            </select> <br>
            <label class = "insert_label"> <b>Ausgewählte Route: </b></label>
            <input readonly class = "alter_input" type = "text" id="Ausgewaehlte_Standort"  name = "Ausgewaehlte_Standort" value = "{{Standorte.first.id}} - {{Standorte.first.Name}} - {{Standorte.first.Adresse}} " placeholder="Auswahl...">
            {% else %}
        <label class = "insert_label"> <b></b></label>
        <label class = "nodata_label"> <b>Kein Standort mit diesem Namen</b></label>
        {% endif %}
    </div> 
</div>
</form> */}