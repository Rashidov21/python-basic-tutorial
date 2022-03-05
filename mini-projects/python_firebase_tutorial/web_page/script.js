// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.6.8/firebase-app-compat.js';
// import { getDatabase } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-database.min.js";

const firebaseConfig = {
    apiKey: "AIzaSyDpoOWQIQGF0ZYJ9QaYj-cG19N3MW2vvhg",
    authDomain: "pybase-9087d.firebaseapp.com",
    projectId: "pybase-9087d",
    storageBucket: "pybase-9087d.appspot.com",
    messagingSenderId: "1064239651081",
    appId: "1:1064239651081:web:f98e55c2174e0b0c5d9bd8",
    measurementId: "G-1E8NF8PYHZ",
    databaseURL: "https://pybase-9087d-default-rtdb.firebaseio.com/"
};

const app = firebase.initializeApp(firebaseConfig);

const db = app.firestore();
// const realTimedDataBase = app.database()

// const auth = app.auth();
// console.log(db.child("main").get())


// Get All FireStore Data
db.collection("users").get().then(querySnapshot => {
    querySnapshot.forEach(doc => {
        let li = document.createElement("li")
        let u = doc.data()
        console.log(u)
        let users = document.querySelector("#users")


        let data = `
        <li id="user" class="panel-block is-active">
            <span class="panel-icon">
                <i class="fas fa-book" aria-hidden="true"></i>
            </span> ${u.name}
            <span> ${u.surname}</span>
            <span> ${u.age}</span>
            <img src='${u.photo}' width='100' height='auto'>
        </li>        
        `
        li.innerHTML = data
        users.appendChild(li)

    });
})