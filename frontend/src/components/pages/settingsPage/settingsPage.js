import React from "react";
import "./settingsPage.css";
import { useNavigate, useLocation } from "react-router-dom";
import Vector from "../../../assets/images/Vector.svg";
import { useTheme } from "../../../hooks/useTheme";

const Settings = () => {
    const { theme, setTheme } = useTheme()
    const navigate = useNavigate();
    const location = useLocation();
    const linkBack = location?.state?.linkBack || "/";
    return (
        <div className="main">
            <div className="main-content">
                <div className="main-content-text">Colour Scheme</div>
                <div className="change-theme-buttons">
                    <button className="green-theme" onClick={() => setTheme('green')}></button>
                    <button className="dark-theme"  onClick={() => setTheme('dark')}></button>
                    <button className="blue-theme"  onClick={() => setTheme('blue')}></button>
                    <button className="wight-theme"  onClick={() => setTheme('light')}></button>
                </div>
            </div>
            <footer>
                <div className="link-back">
                    <img
                        src={Vector}
                        alt="link-back"
                        onClick={() => navigate(linkBack)}
                    />
                </div>
            </footer>
        </div>
    );
};

export default Settings;
