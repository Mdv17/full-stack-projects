import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import ArrowLeft from '../assets/arrow-left.svg?react';


const NotePage = () => {

    let { id } = useParams();
    let [note, setNote] = useState(null);
    // use the useNavigate hook to get the navigate function
    let navigate = useNavigate();
    
    let getNote = async () => {
        if (id === 'new') return

        let response = await fetch(`http://127.0.0.1:8000/api/notes/${id}/`)
        let data = await response.json()
        setNote(data)
    }

    useEffect(() => {
        getNote()
    }, [id])

    let createNote = async () => {
        fetch(`http://127.0.0.1:8000/api/notes/create/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }

    let updateNote = async () => {
        fetch(`http://127.0.0.1:8000/api/notes/${id}/update/`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }


    let deleteNote = async () => {
        fetch(`http://127.0.0.1:8000/api/notes/${id}/delete/`, {
            method: "DELETE",
            headers: {
                'Content-Type': 'application/json'
            }
        })
        navigate('/')
    }

    let handleSubmit = () => {
        if (id !== 'new' && note.body == ''){
            deleteNote()
        } else if (id !== 'new'){
            updateNote()
        } else if (id === 'new' && note.body !== null){
            createNote()
        }
        navigate('/')
    }

    let handleChange = (value) => {
        setNote(note => ({ ...note, 'body': value }))
        console.log('Handle Change:', note)
    }

    return (
        <div className='note'>
            <div className='note-header'>
                <h3>
                    <ArrowLeft onClick={handleSubmit}/>
                </h3>
                {id !== 'new' ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick= {handleSubmit} >Done</button>
                )}
                
                
            </div>
            {/* First thing we want to update the state when my note is updated */}
            {/* We need to pass a function in onChange so that we delay our function call */}
            <textarea onChange={(e) => { handleChange(e.target.value) }} value={note?.body}></textarea>
        </div>
    );
};
export default NotePage;






















// import React, {useState, useEffect} from 'react';
// // importing useParams to replace match.params which is not in React
// import { useParams } from 'react-router-dom';

// const NotePage = () => {
//     //We no longer can use match.params.id thats why we useParams
//     let noteId = useParams().id;
//     let [note, setNote] = useState(null)

//     useEffect(() => {
//         getNote()
//     }, [noteId])

//     let getNote = async ()=> {
        
//         let response = await fetch(`http://127.0.0.1:8000/api/notes/${noteId}/`)
//         console.log(response);
//         let data = await response.json()
//         setNote(data)
//     }

//     // The ? is to say if there is no note.body dont pass an error
//     return (
//         <div>
//             {note ? <p>{note.body}</p> : 'Loading...'}
//         </div>
//     );
// };

// export default NotePage;
