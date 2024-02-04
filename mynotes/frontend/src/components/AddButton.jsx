import React from 'react'
import { Link } from 'react-router-dom'
import AddIcon from '../assets/add.svg?react'

function AddButton() {
  return (
    <Link to = "/note/new" className='floating-button'>
      <AddIcon />
    </Link>
  )
}

export default AddButton
