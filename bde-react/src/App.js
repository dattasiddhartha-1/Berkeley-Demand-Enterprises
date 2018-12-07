import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { BDEMap } from './BDEMap.js'
import * as data from './data.json'
import _ from 'lodash'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stores: []
    };
  }

  componentDidMount() {
      console.log(data)
      this.setState({ stores: _.sampleSize(data.stores, 200) })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <BDEMap stores={this.state.stores}/>
        </header>
      </div>
    );
  }
}

export default App;
