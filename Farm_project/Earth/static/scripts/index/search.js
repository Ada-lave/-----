document.querySelector("#elastic").oninput = function(){
    let val = this.value.trim();



    let CardItems = document.querySelectorAll(".card"); 
    




    CardItems.forEach(function(elem){
        if (elem.innerText.search(val) == -1){
            elem.classList.add('hide');
        }
        else{
            elem.classList.remove('hide');
        }
    });
}