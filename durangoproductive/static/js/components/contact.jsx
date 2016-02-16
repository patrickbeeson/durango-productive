import csrf from '../csrf.js';
import React from 'react';
import ReactDOM from 'react-dom';
import jQuery from 'jquery';

var Message = React.createClass({
  render: function () {
    return (
      <div className={this.props.messageType}>
        <span>{this.props.message}</span>
      </div>
    )
  }
});

var ContactForm = React.createClass({
  getInitialState: function() {
    return {
      name: '',
      email: '',
      message: '',
      url: '',
    };
  },
  handleNameChange: function (e) {
    this.setState({name: e.target.value})
  },
  handleEmailChange: function (e) {
    this.setState({email: e.target.value})
  },
  handleMessageChange: function (e) {
    this.setState({message: e.target.value})
  },
  handleURLChange: function (e) {
    this.setState({url: e.target.value})
  },
  handleFormSubmit: function (e) {
    e.preventDefault();
    var name = this.state.name.trim();
    var email = this.state.email.trim();
    var message = this.state.message.trim();
    var url = this.state.url.trim();
    if (url) {
      var message = 'Have some cheese, spam rat!';
      var messageType = 'flash-error';
      this.props.displayFormError(message, messageType);
      return;
    };
    if (!name || !email || !message) {
      var message = 'All fields are required.';
      var messageType = 'flash-error';
      this.props.displayFormError(message, messageType);
      return;
    };
    var formData = {
      name: name,
      email: email,
      message: message
    };
    this.props.onContactFormSubmit({formData});
    this.setState({
      name: '',
      email: '',
      message: '',
      url: ''
    });
  },
  render: function () {
    return (
      <form onSubmit={this.handleFormSubmit} method="POST">
        <div>
          <label htmlFor="id_name">Name:</label>
          <input onChange={this.handleNameChange} id="id_name" maxLength="200" name="name" type="text" />
        </div>
        <div>
          <label htmlFor="id_email">Email:</label>
          <input onChange={this.handleEmailChange} id="id_email" maxLength="254" name="email" type="email" />
        </div>
        <div>
          <label htmlFor="id_message">Message:</label>
          <textarea onChange={this.handleMessageChange} cols="40" id="id_message" name="message" rows="10" />
          <span className="helptext">Note: Plain text only. All HTML will be stripped and content escaped on submission.</span>
        </div>
        <div className="honeypot">
          <label htmlFor="id_url">Url:</label>
          <input onChange={this.handleURLChange} id="id_url" name="url" type="text" />
        </div>
        <button type="submit" className="btn btn-default">Send</button>
      </form>
    );
  }
});
var ContactFormContainer = React.createClass({
  getInitialState: function() {
    return {
        data: [],
        displayMessage: false,
        message: '',
        messageType: ''
    };
  },
  displayFormError: function (message, messageType) {
    this.setState({
      displayMessage: true,
      message: message,
      messageType: messageType
    })
  },
  onContactFormSubmit: function (formData) {
    jQuery.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: formData,
      success: function(data) {
        this.setState({
            displayMessage: true,
            message: 'Your message has been sent.',
            messageType: 'flash-success'
        });
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
        this.setState({
            displayMessage: true,
            message: 'There was a problem sending your message.',
            messageType: 'flash-error'
        });
      }.bind(this)
    });
  },
  render: function () {
    if (this.state.displayMessage) {
      return (
        <div>
          <Message message={this.state.message} messageType={this.state.messageType} />
          <ContactForm onContactFormSubmit={this.onContactFormSubmit} />
        </div>
      );
    } else {
      return (
        <ContactForm displayFormError={this.displayFormError} onContactFormSubmit={this.onContactFormSubmit} />
      );
    }
  }
});
var communicationCreateUrl = jQuery('#contact_form_container').data('url');
ReactDOM.render(
    <ContactFormContainer url={communicationCreateUrl} />,
    document.getElementById('contact_form_container')
);
