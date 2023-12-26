import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Auth from "../pages/authPage/authPage";
import TeacherPage from "../pages/teacherPage/teacherPage";
import StudentPage from "../pages/studentPage/studentPage";


function App() {
    return (
        <div className="app">
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Auth />}/> 
                    <Route path="/teacher/" element={<TeacherPage />}/> 
                    <Route path="/student/" element={<StudentPage />}/> 
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;