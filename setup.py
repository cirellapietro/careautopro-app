#!/usr/bin/env python3
"""
CareAutoPro v2 - Setup COMPLETO con TUTTI i file
Esegui questo script in GitHub Codespaces per creare l'intero progetto
"""

import os
import sys

class Colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'

def p(text, color=Colors.NC):
    print(f"{color}{text}{Colors.NC}")

def write_file(path, content):
    try:
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        p(f"❌ Errore: {path} - {e}", Colors.RED)
        return False

p("=" * 70, Colors.CYAN)
p("🚗 CareAutoPro v2 - Setup COMPLETO AUTOMATICO", Colors.BLUE)
p("=" * 70, Colors.CYAN)
print()

# Crea struttura
p("📁 Creazione struttura...", Colors.BLUE)
for d in ["src/components/Auth", "src/components/Dashboard", "src/components/GPS",
          "src/components/Veicoli", "src/components/Settings", "src/components/Ads",
          "src/contexts", "src/lib", "public/icons"]:
    os.makedirs(d, exist_ok=True)
p("✅ Struttura creata\n", Colors.GREEN)

# Counter
count = 0

# ==================== FILE DI CONFIGURAZIONE ====================

p("📝 Creazione file di configurazione...", Colors.BLUE)

# .gitignore
write_file(".gitignore", """# Logs
logs
*.log
npm-debug.log*

# Dependencies
node_modules/
/.pnp
.pnp.js

# Production
/dist
/build

# Misc
.DS_Store
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Editor
.vscode/
.idea/
*.swp
*.swo

# Vercel
.vercel
""")
count += 1

# package.json
write_file("package.json", """{
  "name": "careautopro-v2",
  "private": true,
  "version": "2.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.39.3",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.3",
    "date-fns": "^3.3.1",
    "lucide-react": "^0.320.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.33",
    "tailwindcss": "^3.4.1",
    "vite": "^5.0.12",
    "vite-plugin-pwa": "^0.17.5"
  }
}
""")
count += 1

# .env
write_file(".env", """VITE_SUPABASE_URL=https://jamttxwhexlvbkjccrqm.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImphbXR0eHdoZXhsdmJramNjcnFtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTM2NTE5MDIsImV4cCI6MjA2OTIyNzkwMn0.MkQarY2dOUuwhFnOdaLHqb6idFocTGSfZKjqVoeDYBs
VITE_APP_NAME=CareAutoPro
VITE_APP_VERSION=2.0.0
""")
count += 1

# vite.config.js
write_file("vite.config.js", """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: { port: 3000 }
});
""")
count += 1

# tailwind.config.js  
write_file("tailwind.config.js", """export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: { extend: {} },
  plugins: []
}
""")
count += 1

# postcss.config.js
write_file("postcss.config.js", """export default {
  plugins: { tailwindcss: {}, autoprefixer: {} }
}
""")
count += 1

# vercel.json
write_file("vercel.json", """{
  "rewrites": [{"source": "/(.*)", "destination": "/index.html"}]
}
""")
count += 1

# index.html
write_file("index.html", """<!DOCTYPE html>
<html lang="it">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#1e40af" />
    <title>CareAutoPro</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""")
count += 1

# manifest.json
write_file("manifest.json", """{
  "name": "CareAutoPro",
  "short_name": "CareAuto",
  "start_url": "/",
  "display": "standalone",
  "theme_color": "#1e40af"
}
""")
count += 1

p(f"✅ {count} file di configurazione creati\n", Colors.GREEN)

# ==================== FILE REACT ====================

p("⚛️  Creazione file React (questo richiede un momento)...", Colors.BLUE)

# src/main.jsx
write_file("src/main.jsx", """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
""")
count += 1

# src/index.css
write_file("src/index.css", """@tailwind base;
@tailwind components;
@tailwind utilities;

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  background: #f9fafb;
  color: #111827;
}

#root {
  min-height: 100vh;
}
""")
count += 1

# src/lib/supabase.js
write_file("src/lib/supabase.js", """import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseAnonKey, {
  auth: {
    autoRefreshToken: true,
    persistSession: true,
    detectSessionInUrl: true
  }
});

export const getCurrentUser = async () => {
  const { data: { user }, error } = await supabase.auth.getUser();
  if (error) throw error;
  return user;
};

export const signOut = async () => {
  const { error } = await supabase.auth.signOut();
  if (error) throw error;
};

export const signInWithEmail = async (email, password) => {
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) throw error;
  return data;
};

export const signUpWithEmail = async (email, password, metadata = {}) => {
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
    options: { data: metadata }
  });
  if (error) throw error;
  return data;
};

export const signInWithProvider = async (provider) => {
  const { data, error } = await supabase.auth.signInWithOAuth({
    provider,
    options: { redirectTo: window.location.origin }
  });
  if (error) throw error;
  return data;
};

export const onAuthStateChange = (callback) => {
  return supabase.auth.onAuthStateChange((event, session) => {
    callback(event, session);
  });
};
""")
count += 1

# src/contexts/AuthContext.jsx
write_file("src/contexts/AuthContext.jsx", """import { createContext, useContext, useState, useEffect } from 'react';
import { supabase, getCurrentUser, signOut, onAuthStateChange } from '../lib/supabase';

const AuthContext = createContext({});

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    checkUser();
    const { data: { subscription } } = onAuthStateChange(async (event, session) => {
      if (session?.user) {
        setUser(session.user);
        await loadUserProfile(session.user.id);
      } else {
        setUser(null);
        setProfile(null);
      }
      setLoading(false);
    });
    return () => subscription?.unsubscribe();
  }, []);

  const checkUser = async () => {
    try {
      const currentUser = await getCurrentUser();
      setUser(currentUser);
      if (currentUser) await loadUserProfile(currentUser.id);
    } catch (error) {
      console.error('Error checking user:', error);
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  const loadUserProfile = async (userId) => {
    try {
      const { data, error } = await supabase
        .from('utenti')
        .select('*')
        .eq('utente_id', userId)
        .single();
      if (error && error.code !== 'PGRST116') throw error;
      setProfile(data);
    } catch (error) {
      console.error('Error loading profile:', error);
    }
  };

  const logout = async () => {
    try {
      await signOut();
      setUser(null);
      setProfile(null);
    } catch (error) {
      console.error('Logout error:', error);
      throw error;
    }
  };

  return (
    <AuthContext.Provider value={{ user, profile, loading, logout, refreshProfile: () => user ? loadUserProfile(user.id) : null }}>
      {children}
    </AuthContext.Provider>
  );
};
""")
count += 1

# src/App.jsx
write_file("src/App.jsx", """import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import Login from './components/Auth/Login';
import Register from './components/Auth/Register';
import Dashboard from './components/Dashboard/Dashboard';
import AddVeicolo from './components/Veicoli/AddVeicolo';
import Settings from './components/Settings/Settings';

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();
  if (loading) return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  if (!user) return <Navigate to="/login" replace />;
  return children;
}

function PublicRoute({ children }) {
  const { user, loading } = useAuth();
  if (loading) return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  if (user) return <Navigate to="/dashboard" replace />;
  return children;
}

function AppRoutes() {
  return (
    <Routes>
      <Route path="/login" element={<PublicRoute><Login /></PublicRoute>} />
      <Route path="/register" element={<PublicRoute><Register /></PublicRoute>} />
      <Route path="/dashboard" element={<ProtectedRoute><Dashboard /></ProtectedRoute>} />
      <Route path="/veicoli/nuovo" element={<ProtectedRoute><AddVeicolo /></ProtectedRoute>} />
      <Route path="/settings" element={<ProtectedRoute><Settings /></ProtectedRoute>} />
      <Route path="/" element={<Navigate to="/dashboard" replace />} />
      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}

export default function App() {
  return (
    <Router>
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </Router>
  );
}
""")
count += 1

p(f"✅ {count - 9} file React core creati", Colors.GREEN)

# ==================== COMPONENTI ====================

p("🎨 Creazione componenti...", Colors.BLUE)

# Login (versione compatta ma funzionale)
write_file("src/components/Auth/Login.jsx", """import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signInWithEmail, signInWithProvider } from '../../lib/supabase';
import { Mail, Lock, LogIn, Chrome, Facebook } from 'lucide-react';

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleEmailLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await signInWithEmail(email, password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.message || 'Errore durante il login');
    } finally {
      setLoading(false);
    }
  };

  const handleSocialLogin = async (provider) => {
    setError('');
    setLoading(true);
    try {
      await signInWithProvider(provider);
    } catch (err) {
      setError(err.message);
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 px-4">
      <div className="max-w-md w-full bg-white p-8 rounded-2xl shadow-xl">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-900">CareAutoPro</h2>
          <p className="text-sm text-gray-600 mt-2">Gestisci i tuoi veicoli</p>
        </div>

        {error && <div className="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-6 text-sm">{error}</div>}

        <form onSubmit={handleEmailLogin} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Email</label>
            <div className="relative">
              <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input type="email" required value={email} onChange={(e) => setEmail(e.target.value)}
                className="pl-10 w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="tua@email.com" />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input type="password" required value={password} onChange={(e) => setPassword(e.target.value)}
                className="pl-10 w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="••••••••" />
            </div>
          </div>

          <button type="submit" disabled={loading}
            className="w-full flex justify-center items-center py-3 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 transition-colors">
            <LogIn className="h-5 w-5 mr-2" />
            {loading ? 'Accesso...' : 'Accedi'}
          </button>
        </form>

        <div className="relative my-6">
          <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-gray-300"></div></div>
          <div className="relative flex justify-center text-sm"><span className="px-2 bg-white text-gray-500">Oppure</span></div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <button onClick={() => handleSocialLogin('google')} disabled={loading}
            className="flex items-center justify-center py-3 px-4 border border-gray-300 rounded-lg bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50">
            <Chrome className="h-5 w-5 mr-2 text-red-500" />Google
          </button>
          <button onClick={() => handleSocialLogin('facebook')} disabled={loading}
            className="flex items-center justify-center py-3 px-4 border border-gray-300 rounded-lg bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50">
            <Facebook className="h-5 w-5 mr-2 text-blue-600" />Facebook
          </button>
        </div>

        <div className="text-center mt-6">
          <p className="text-sm text-gray-600">
            Non hai un account?{' '}
            <button onClick={() => navigate('/register')} className="font-medium text-blue-600 hover:text-blue-500">
              Registrati
            </button>
          </p>
        </div>
      </div>
    </div>
  );
}
""")
count += 1

# Register (versione compatta)
write_file("src/components/Auth/Register.jsx", """import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { signUpWithEmail, supabase } from '../../lib/supabase';
import { Mail, Lock, User } from 'lucide-react';

export default function Register() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ nominativo: '', email: '', password: '', confirmPassword: '' });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    if (formData.password !== formData.confirmPassword) {
      setError('Le password non coincidono');
      setLoading(false);
      return;
    }

    try {
      const { data: authData, error: authError } = await signUpWithEmail(
        formData.email,
        formData.password,
        { nominativo: formData.nominativo }
      );
      if (authError) throw authError;

      await supabase.from('utenti').insert({
        utente_id: authData.user.id,
        nominativo: formData.nominativo,
        email: formData.email,
        abilitagps: false
      });

      setSuccess(true);
      setTimeout(() => navigate('/login'), 3000);
    } catch (err) {
      setError(err.message || 'Errore durante la registrazione');
    } finally {
      setLoading(false);
    }
  };

  if (success) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 px-4">
        <div className="max-w-md w-full bg-white p-8 rounded-2xl shadow-xl text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">Registrazione completata!</h2>
          <p className="text-gray-600 mb-6">Controlla la tua email per confermare l'account.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 px-4 py-12">
      <div className="max-w-md w-full bg-white p-8 rounded-2xl shadow-xl">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-gray-900">Crea Account</h2>
        </div>

        {error && <div className="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-6 text-sm">{error}</div>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Nome e Cognome *</label>
            <div className="relative">
              <User className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input type="text" name="nominativo" required value={formData.nominativo} onChange={handleChange}
                className="pl-10 w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="Mario Rossi" />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Email *</label>
            <div className="relative">
              <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input type="email" name="email" required value={formData.email} onChange={handleChange}
                className="pl-10 w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="mario.rossi@email.com" />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Password *</label>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input type="password" name="password" required value={formData.password} onChange={handleChange}
                className="pl-10 w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="••••••••" />
            </div>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Conferma Password *</label>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400" />
              <input type="password" name="confirmPassword" required value={formData.confirmPassword} onChange={handleChange}
                className="pl-10 w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
                placeholder="••••••••" />
 
