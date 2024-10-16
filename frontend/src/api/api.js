import axios from 'axios';
import { DB_URL } from '../utils/constants';

class Api {

    async getBusFactor(teamId) {
        try {
            const response = await axios.get(`${DB_URL}/api/v1/dashboard/bus_factor/`, {
                params: { team: teamId }, // Используйте params для добавления query параметров
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            });
            return response.data;
        } catch (error) {
            throw new Error(`Ошибка: ${error.response?.status} ${error.response?.statusText}`);
        }
    }

    async getTeamNames() {
        try {
            const response = await axios.get(`${DB_URL}/api/v1/teams`, {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            });
            return response.data;
        } catch (error) {
            throw new Error(`Ошибка: ${error.response?.status} ${error.response?.statusText}`);
        }
    }

    async getAllStaff(teamId) {
        try {
            const response = await axios.get(`${DB_URL}/api/v1/dashboard/suitability_position/`, {
                params: { team: teamId },
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
            });
            return response.data;
        } catch (error) {
            throw new Error(`Ошибка: ${error.response?.status} ${error.response?.statusText}`);
        }
    }
}

const api = new Api();
export default api;