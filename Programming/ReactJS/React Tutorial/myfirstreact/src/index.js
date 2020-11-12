import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.js';
import Kotse from './App2.js'

const myfirstelement = (
<table>
<tr>
  <th>Name</th>
</tr>
<tr>
  <td>John</td>
</tr>
<tr>
  <td>Elsa</td>
</tr>
</table>
);

const mysecondelement = <p>HATDOGGGGGG</p>
const third = <p>React with a {100-1}% better when using JSX lmao</p>
const fourth = (
  <div>
  <h1>1</h1>
  <h2>2</h2>
  </div>
);

class Car extends React.Component {
  render() { //Returns an html
    return <h2>Hi, I am a {this.props.color} Car!</h2>;
  }
}

/*
class Car extends React.Component {
  render() {
    return <h2>I am a {this.props.color} Car!</h2>;
  }
}

ReactDOM.render(<Car color="red"/>, document.getElementById('root'));
*/

//Can call between classes using components
class Garage extends React.Component {
  render() {
    const carcolor = "Red HAHAHA"
    return (
      <div>
      <h1>Who lives in my Garage?</h1>
      <Car color={carcolor}/>
      </div>
    );
  }
}



//ReactDOM.render(variable, document.getMethod('Value'))

ReactDOM.render(myfirstelement, document.getElementById('root'));
ReactDOM.render(mysecondelement, document.getElementById('victim2'));
ReactDOM.render(third, document.getElementById('victim3'));
ReactDOM.render(<Car color="Black"/>, document.getElementById('victim4'));
ReactDOM.render(fourth, document.getElementById('5'));
ReactDOM.render(<Garage />, document.getElementById('6'));
ReactDOM.render(<App />, document.getElementById('7')); //this should be the orig thing
ReactDOM.render(<Kotse />, document.getElementById('Kotse'));

