import React from "react";
import "./studentPage.css";
import Settings from "../../../assets/images/Settings.svg";
import Vector from "../../../assets/images/Vector.svg"

const StudentPage = () => {
    return (
        <div className="student-main-page">
            <nav>
                <div className="settings">
                    <img src={Settings} alt="settings" />
                </div>
            </nav>
            <div className="main-content">
                <div>
                    <div className="button-description">Theme</div>
                    <div className="theme-buttons">
                        <button className="choice-button">Math</button>
                        <button className="choice-button">English</button>
                        <button className="choice-button">Nature</button>
                    </div>
                </div>
                <div>
                    <div className="button-description difficulty">Difficulty</div>
                    <div className="difficluty-buttons">
                        <button className="choice-button">Easy</button>
                        <button className="choice-button">Medium</button>
                        <button className="choice-button">Hard</button>
                    </div>
                </div>
                <button className="complete-random-exercise">
                    Complete random level
                </button>
            
            </div>
            <footer>
            <div className="logout">
                    <img src={Vector} alt="logout" />
                </div>
            </footer>
        </div>
    );
};

export default StudentPage;