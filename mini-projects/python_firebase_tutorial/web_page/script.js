// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.6.8/firebase-app-compat.js';
// import { getDatabase } from "https://www.gstatic.com/firebasejs/9.6.8/firebase-database.min.js";

const firebaseConfig = {
//    YOUR API DATA
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