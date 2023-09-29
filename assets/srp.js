let codeButtons = document.getElementsByClassName('vomv');
let arr = []
let failSafe = 0;
let extraFailSafe = 0;
// console.log('1')
function replaceOBD(code, messg) {
    document.getElementById("codeTit").innerHTML = code;
    document.getElementById("codeMessg").innerHTML = messg;
}
// console.log('2')

let loads = setInterval(() => {
    if (codeButtons.length > 1 && failSafe == 0) {
        gen();
        let st = document.getElementById('clkState');
        st.innerHTML = "Ready";
        st.style.color = "green";
        failSafe = 1;
    } else if (codeButtons.length > 1 && failSafe == 1){
        clearInterval(loads);
    }
}, 3600)

function gen() {
    for (let i=0;i<codeButtons.length;i++) {
        let idd = codeButtons[i].id
        let updJson = {
            "name" : idd.replace("code-but_", ""),
            "data" : codeButtons[i].value
        }
            console.log('hello');
            arr.push(updJson);
    }
        // console.log('3')
    console.log(arr[codeButtons.length - 1]);
    for (let j=0; j<codeButtons.length;j++) {
                // console.log(`added: ${codeButtons[j].id}`)
        document.getElementById(codeButtons[j].id).addEventListener('click', () => {
            // console.log(`added: ${codeButtons[j].id} and ${arr[j].data}`)
            replaceOBD(arr[j].name, arr[j].data)
        })
    }

    


        // console.log('4')
    
}
