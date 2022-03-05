// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.6.8/firebase-app-compat.js';
// import { getDatabase } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-database.min.js";

const firebaseConfig = {
    apiKey: "AIzaSyBfePZU1LMCmrwxFqLYXiQF_n132SdZhC4",
    authDomain: "fruitsbase.firebaseapp.com",
    databaseURL: "https://fruitsbase-default-rtdb.firebaseio.com",
    projectId: "fruitsbase",
    storageBucket: "fruitsbase.appspot.com",
    messagingSenderId: "445383361070",
    appId: "1:445383361070:web:4210d09aabe8622619d5bf",
    measurementId: "G-QCV1XJRVHR"
};

const app = firebase.initializeApp(firebaseConfig);

const db = app.firestore();
// const realTimedDataBase = app.database()

// const auth = app.auth();
// console.log(db.child("main").get())


// Get All FireStore Data
db.collection("fruits").get().then(querySnapshot => {
    querySnapshot.forEach(doc => {

        let li = document.createElement("li")
        li.innerHTML = `
            <h3><b>${doc.data().name}</b></h3>
            <h3><b>${doc.data().price}</b></h3>
            <img src='${doc.data().photo}' width='200' height='auto'>
        `;
        document.querySelector("#fruits").appendChild(li)

    });
})