import { useState } from 'react'
import './BirthdayQuestion.css'

function BirthdayQuestion({ onResponse, isLoading }) {
  return (
    <div className="question-container">
      
      <h1>Do you have any boyfriend?</h1>
      <p className="subtitle">Please be honest...</p>
      
      <div className="button-group">
        <button 
          className="btn btn-yes" 
          onClick={() => onResponse(true)}
          disabled={isLoading}
        >
          {isLoading ? '⏳ Processing...' : 'Yes'}
        </button>
        <button 
          className="btn btn-no" 
          onClick={() => onResponse(false)}
          disabled={isLoading}
        >
          {isLoading ? '⏳ Processing...' : 'No'}
        </button>
      </div>
    </div>
  )
}

export default BirthdayQuestion
