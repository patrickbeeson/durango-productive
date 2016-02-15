import React from 'react';
import ReactDOM from 'react-dom';
import jQuery from 'jquery';

var ProjectContainer = React.createClass({
    getInitialState: function () {
        return {data: {assets: []}};
    },
    componentDidMount: function() {
    jQuery.ajax({
        url: this.props.url,
        dataType: 'json',
        cache: false,
        success: function(data) {
            this.setState({data: data});
        }.bind(this),
        error: function(xhr, status, err) {
            console.error(this.props.url, status, err.toString());
        }.bind(this)
        });
    },
    render: function () {
        return (
            <Project data={ this.state.data } />
        );
    }
});
var Project = React.createClass({
    render: function() {
        return (
            <li className="footer_past_projects">
                <a href="/work/">
                    <img src={ this.props.data.lead_art } alt={ this.props.data.client_name } />
                    Past Projects
                </a>
            </li>
        );
    }
});
var featuredContainerUrl = jQuery('#project_featured').data('url');
ReactDOM.render(
    <ProjectContainer url={ featuredContainerUrl } />,
    document.getElementById('project_featured')
);
