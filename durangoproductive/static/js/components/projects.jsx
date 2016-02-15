import React from 'react';
import ReactDOM from 'react-dom';
import jQuery from 'jquery';

var ProjectListContainer = React.createClass({
    loadProjectsFromServer: function() {
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
    getInitialState: function () {
        return {data: []};
    },
    componentDidMount: function() {
        this.loadProjectsFromServer();
    },
    render: function () {
        return (
            <ProjectList data={this.state.data} />
        );
    }
});
var ProjectList = React.createClass({
    render: function() {
        var projectNodes = this.props.data.map(function (project) {
            return (
                <Project key={ project.pk } client_name={ project.client_name } lead_art={ project.lead_art } project_detail={ project.project_detail.self } />
            );
        });
        return (
            <ul className="project_list">
                {projectNodes}
            </ul>
        );
    }
});
var Project = React.createClass({
    render: function() {
        return (
            <li className="project">
                <a href={ this.props.project_detail }>
                    <img src={ this.props.lead_art } alt="More about this project" />
                    { this.props.client_name }
                </a>
            </li>
        )
    }
});
var projectsUrl = jQuery('#projects').data('url');
ReactDOM.render(
    <ProjectListContainer url={ projectsUrl } />,
    document.getElementById('projects')
);
