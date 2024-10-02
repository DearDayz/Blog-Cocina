import React from 'react'
import './Loginformulario.css'
import { FaUser, FaLock } from "react-icons/fa";


export const Loginformulario = () => {
    return (
        <div className='wrapper'>
            <form action=''>
                <h1>Login</h1>
                <div className="input-box">
                    <input type="text" placeholder='Nombre de Usuario' required />
                    <FaUser className='icon' />
                </div>
                <div className="input-box">
                    <input type="password" placeholder='Contraseña' required />
                    <FaLock className='icon' />
                </div>

                <div className="olvidar_contrasena">
                    <a href="#">¿Se olvidó la contraseña?</a>
                </div>

                <button type='submit'>Entrar</button>

                <div className="registrar_cuenta">
                    <p>¿Queee? ¿No ha registrado una cuenta? <a href="#">¡Voy a crearlo!</a></p>
                </div>
            </form>
        </div>
    )
}
