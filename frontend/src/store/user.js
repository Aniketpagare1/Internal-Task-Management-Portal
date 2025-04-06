import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: JSON.parse(localStorage.getItem('user')) || null,
  }),

  getters: {
    isLoggedIn: (state) => !!state.token,
    isManager: (state) => state.user?.role === 'manager',
    isEmployee: (state) => state.user?.role === 'employee',
  },

  actions: {
    async login(credentials) {
      const response = await axios.post('http://localhost:5000/api/login', credentials);
      this.token = response.data.token;
      this.user = response.data.user;
      localStorage.setItem('token', this.token);
      localStorage.setItem('user', JSON.stringify(this.user));
      axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
    },

    async logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      delete axios.defaults.headers.common['Authorization'];
    },

    async register(data) {
      await axios.post('http://localhost:5000/api/register', data);
    }
  }
});
