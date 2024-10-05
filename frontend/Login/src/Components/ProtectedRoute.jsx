import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"; // Ver constans.js para saber su uso
import { useState, useEffect } from "react";

// Función que nos va a permitir mostrale la vista (que sería "children" que se le pasa a la función)
// Solo si está logeado (Osea tiene el token JWT)

function ProtectedRoute({ children }) {
    const [isAuthorized, setIsAuthorized] = useState(null); // isAuthorized guarda el estado (null por defecto), y setIsAuthorized lo establece

    // Se verifica si hay el usuario está autorizado para ver la vista, si hay un error se toma como un False
    useEffect(() => {
        auth().catch(() => setIsAuthorized(false))
    }, [])

    const refreshToken = async () => {

        // Obteniendo el refresh token se intenta generar uno nuevo usando una api del backend
        const refreshToken = localStorage.getItem(REFRESH_TOKEN);
        try {
            const res = await api.post("/api/token/refresh/", {
                refresh: refreshToken,
            });
            // Si se genera correctamente se actualiza el token expirado y se autoriza al usuario
            if (res.status === 200) {
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            } else {
                setIsAuthorized(false)
            }
        } catch (error) {
            console.log(error);
            setIsAuthorized(false);
        }
    };

    // Función que verifica si el usuario esta logeado/autorizado
    const auth = async () => {
        // Se verifica si tenemos el token
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (!token) {
            setIsAuthorized(false);
            return;
        }

        // Teniendo el token se verifica si está expirado
        const decoded = jwtDecode(token);
        const tokenExpiration = decoded.exp;
        const now = Date.now() / 1000;

        if (tokenExpiration < now) {
            await refreshToken();
        } else {
            setIsAuthorized(true);
        }
    };

    if (isAuthorized === null) {
        // Si es null es porque no se han cargado las funciones anteriores
        return <div>Loading...</div>;
    }

    // Si el user está autorizado (tiene el token) retorna el children o vista protegida
    // Si no lo está se redirige al login
    return isAuthorized ? children : <Navigate to="/login" />;
}


// Función que recibe una vista (children) y los permisos necesarios para acceder a esa vista (permissionsRequired)
// Y verifica si el usuario tiene los permisos necesarios
function VerifyPermissions(permissionsRequired, { children }) {
    const res = api.get()
}

export default ProtectedRoute;