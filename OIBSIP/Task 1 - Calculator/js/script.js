const display = document.querySelector(".display");
const buttons = document.querySelectorAll("button");
const specialChars = ["%","*","/","-","+","="];
let output = "";
const calculate = (buttonValue) => {
    if(buttonValue === "=" && output !== "")
    {
        output = eval(output.replace("%","/100"));
    }
    else if(buttonValue==="AC")
    {
        output="";
    }
    else if(buttonValue === "DEL")
    {
        output = output.toString().slice(0,-1);
    }
    else
    {
        if(output==="" && specialChars.includes(buttonValue)) return;
        output += buttonValue;
    }
    // console.log(buttonValue);
    display.value=output;
};
//console.log(display,buttons)
buttons.forEach((button) => {
    button.addEventListener("click",(e) => calculate(e.target.dataset.value));
});