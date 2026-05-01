import { useState } from 'react'
import axios from 'axios'
import BirthdayQuestion from './components/BirthdayQuestion'
import Proposal from './components/Proposal'
import './App.css'

function App() {
  const [currentPage, setCurrentPage] = useState('question')
  const [isLoading, setIsLoading] = useState(false)

  const handleBirthdayResponse = async (hasBoyfriend) => {
    setIsLoading(true)
    try {
      const response = await axios.post('http://localhost:8000/api/has-boyfriend', {
        has_boyfriend: hasBoyfriend
      })
      
      if (hasBoyfriend) {
        // Show rejection message
        alert(response.data.message)
      } else {
        // Move to proposal page
        setCurrentPage('proposal')
      }
    } catch (error) {
      console.error('Error:', error)
      alert('Error processing response')
    } finally {
      setIsLoading(false)
    }
  }

  const handleProposalResponse = async (accepted) => {
    setIsLoading(true)
    try {
      const response = await axios.post('http://localhost:8000/api/proposal-response', {
        proposal_response: accepted
      })
      
      if (accepted) {
        alert('💕 ' + response.data.message)
        setCurrentPage('success')
      }
    } catch (error) {
      console.error('Error:', error)
      alert('Error processing response')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="app">
      {currentPage === 'question' && (
        <BirthdayQuestion onResponse={handleBirthdayResponse} isLoading={isLoading} />
      )}
      {currentPage === 'proposal' && (
        <Proposal onResponse={handleProposalResponse} isLoading={isLoading} />
      )}
      {currentPage === 'success' && (
        <div className="success-page">
          <h1>💕 Congratulations! 💕</h1>
          <p>She said YES!</p>
          <p className="message">You have successfully proposed!</p>
        </div>
      )}
    </div>
  )
}

export default App
