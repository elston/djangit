// @flow
// ..
import React from 'react'
import ReactDOM from 'react-dom'
// ..
import Root from './components/Root'

// ..
function square(n: number): number {
  return n * n
}

console.log(square("2"))
// ..
ReactDOM.render(<Root/>, document.getElementById('root'))