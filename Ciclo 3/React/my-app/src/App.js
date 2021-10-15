import React, {Component} from 'react';
import './App.css';

class App extends Component{
  render(){
    const anno = 2021;
    const persona = {
      nombre:'pepe',
      edad:56
    }
    return(
      <div>
        <h1>Título</h1>
        <hr/>
        <p>Estamos en el año {anno}</p>
        <p>Su nombre es {persona.nombre} y su edad es {persona.edad}</p>
      </div>
    )
  }
}

export default App;
