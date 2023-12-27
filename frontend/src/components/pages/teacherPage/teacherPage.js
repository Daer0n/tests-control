import React, { useState } from "react";
import "./teacherPage.css";
import api from "../../../api/api";
import { useNavigate } from "react-router-dom";
import Settings from "../../../assets/images/Settings.svg";
import Vector from "../../../assets/images/Vector.svg";

const TeacherPage = () => {
    const navigate = useNavigate();
    const [selectedTheme, setSelectedTheme] = useState("");
    const [selectedLevel, setSelectedLevel] = useState("");

    const handleLogout = async () => {
        await api.post("/auth/logout/");
        navigate("/");
    };

    const handleThemeSelection = (theme) => {
        setSelectedTheme(theme);
    };

    const handleLevelSelection = (level) => {
        setSelectedLevel(level);
    };
    return (
        <div className="student-main-page">
            <nav>
                <div
                    className="settings"
                    onClick={() =>
                        navigate("/settings", {
                            state: { linkBack: "/teacher/" },
                        })
                    }
                >
                    <img src={Settings} alt="settings" />
                </div>
            </nav>
            <div className="main-content">
                <div>
                    <div className="button-description">Theme</div>
                    <div className="theme-buttons">
                        <button
                            className={`choice-button ${
                                selectedTheme === "Math" ? "selected" : ""
                            }`}
                            onClick={() => handleThemeSelection("Math")}
                        >
                            Math
                        </button>
                        <button
                            className={`choice-button ${
                                selectedTheme === "English" ? "selected" : ""
                            }`}
                            onClick={() => handleThemeSelection("English")}
                        >
                            English
                        </button>
                        <button
                            className={`choice-button ${
                                selectedTheme === "Nature" ? "selected" : ""
                            }`}
                            onClick={() => handleThemeSelection("Nature")}
                        >
                            Nature
                        </button>
                    </div>
                </div>
                <div>
                    <div className="button-description difficulty">
                        Difficulty
                    </div>
                    <div className="difficluty-buttons">
                        <button
                            className={`choice-button ${
                                selectedLevel === "Easy" ? "selected" : ""
                            }`}
                            onClick={() => handleLevelSelection("Easy")}
                        >
                            Easy
                        </button>
                        <button
                            className={`choice-button ${
                                selectedLevel === "Medium" ? "selected" : ""
                            }`}
                            onClick={() => handleLevelSelection("Medium")}
                        >
                            Medium
                        </button>
                        <button
                            className={`choice-button ${
                                selectedLevel === "Hard" ? "selected" : ""
                            }`}
                            onClick={() => handleLevelSelection("Hard")}
                        >
                            Hard
                        </button>
                    </div>
                </div>
                <button className="create-exercise">Create exercise</button>
            </div>
            <footer>
                <div className="logout" onClick={handleLogout}>
                    <img src={Vector} alt="logout" />
                </div>
            </footer>
        </div>
    );
};

export default TeacherPage;
