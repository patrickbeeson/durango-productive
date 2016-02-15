import React from 'react';
import ReactDOM from 'react-dom';
import jQuery from 'jquery';

var ProjectContainer = React.createClass({
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
        return {data: {assets: []}};
    },
    componentDidMount: function() {
        this.loadProjectsFromServer();
    },
    render: function () {
        return (
            <Project data={ this.state.data } />
        );
    }
});
var Project = React.createClass({
    rawMarkup: function() {
        var rawMarkup = this.props.data.description_html;
        return { __html: rawMarkup };
    },
    render: function() {
        var assetNodes = this.props.data.assets.map(function (asset) {
            return (
                <Asset key={ asset.pk } art={ asset.art } project={ asset.project } description={ asset.description } />
            );
        });
        return (
            <div>
                <header>
                    <h2 className="lead_head">{ this.props.data.client_name }</h2>
                </header>
                <span dangerouslySetInnerHTML={ this.rawMarkup() } />
                <ul className="project_asset_list">
                    { assetNodes }
                </ul>
            </div>
        );
    }
});
var Asset = React.createClass({
    render: function() {
        return (
            <li className="asset">
                <span className="asset_description">{ this.props.project }{ this.props.description }</span>
                <a href={ this.props.art } data-title={ this.props.project } data-lightbox="roadtrip">
                    <img src={ this.props.art } alt={ this.props.description } />
                </a>
            </li>
        )
    }
});
var projectDetailUrl = jQuery('#project_indiv').data('url');
ReactDOM.render(
    <ProjectContainer url={ projectDetailUrl } />,
    document.getElementById('project_indiv')
);
