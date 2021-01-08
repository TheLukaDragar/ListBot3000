
    //assuming this is the first DOM element with "list-group" class.

//document.querySelector(".list-group").innerHTML += "<li class="+"list-group-item"+">your content</li>";

    /* 
    or,
    
    document.getElementsByClassName("list-group")[0].innerHTML += "<li>your content</li>";
    
    or, 
    
    var li = document.createElement("li");
    var inside = document.createTextNode("your text");
    li.appendChild(inside);
    document.querySelector(".list-group").appendChild(li); 
    
    */



/*
document.getElementById('txt').onchange = function () {

    var file = this.files[0];

    var reader = new FileReader();
    reader.onload = function (progressEvent) {
        // Entire file
        console.log(this.result);

        // By lines
        var lines = this.result.split('\n');
        for (var line = 0; line < lines.length; line++) {
            console.log(lines[line]);

            var li = document.createElement("li");
            var inside = document.createTextNode(lines[line]);
            li.appendChild(inside);
            document.querySelector(".list-group").appendChild(li); 
        }
    };
    reader.readAsText(file);
};
*/


function readTextFile(file) {
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4) {
            if (rawFile.status === 200 || rawFile.status === 0) {
                var allText = rawFile.responseText;
                //alert(allText);
                allText=allText.split('\n');
                if (allText.length-1==0) {
                    document.querySelector(".list-group").innerHTML =
                        "<li class=" + "list-group-item p1 style=" + "\" margin-top: 1rem; background-color:#2c2f33;  color:#fff; word-wrap: break-word; \"" + ">" + "Questions? No, none so far." + "</li>";

                    
                }else {


                
            
               
                var finhtml;
                    
                for (var i = 0; i < allText.length-1; i++) {

                    var tex= allText[i]
                    finhtml+= "<li class=" + "list-group-item p1 style=" + "\" margin-top: 1rem; background-color:#2c2f33;  color:#fff; word-wrap: break-word; \"" + ">" + tex + "</li>";

                    //code here using lines[i] which will give you each line
                }
                document.querySelector(".list-group").innerHTML=finhtml
            }
            
            }
        }
    };
    rawFile.send(null);
}
setInterval(function () {
    // This will be executed every 5 seconds
    readTextFile("/questions.txt")
}, 1000); // 5000 milliseco
