import React, {useState, useEffect} from 'react'
import ListItem from '../components/ListItem'
import AddButton from '../components/AddButton'


const NotesListPage = () => {

    // useState returns the value i.e notes and way to update the notes
    let [notes, setNotes] = useState([])

    // useEffect is another hook that takes in an arrow (=>) function 
    useEffect(()=> {

        // a function to get our notes
    // in order to use a weight we are supposed to use async function
        let getNotes = async () => {
            //await will jus wait for the data 
            let response = await fetch('http://127.0.0.1:8000/api/notes/')
            // if you dont use await we gonna return a promise not a data. It slows down the app so we get the data
            let data = await response.json()
            console.log('DATA:', data)
            setNotes(data)
        }

        getNotes()
        // [] is for passing a list of dependancies
    }, [])


    
    return (
        <div className='notes'>
            <div className='notes-header'>
                <h2 className='notes-title'>&#9782; Notes</h2>
                <p className='notes-count'>{notes.length}</p>
            </div>

            <div className="notes-list">
                {/* to loop all our notes and state current index */}
                {notes.map((note, index) => {
                    return <ListItem key={index} note={note}/>
                })}
            </div>
            <AddButton />
        </div>
    )
}

export default NotesListPage
