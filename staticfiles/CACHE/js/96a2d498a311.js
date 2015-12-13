var ProjectContainer=React.createClass({displayName:"ProjectContainer",loadProjectsFromServer:function(){$.ajax({url:this.props.url,dataType:'json',cache:false,success:function(data){this.setState({data:data});}.bind(this),error:function(xhr,status,err){console.error(this.props.url,status,err.toString());}.bind(this)});},getInitialState:function(){return{data:{assets:[]}};},componentDidMount:function(){this.loadProjectsFromServer();setInterval(this.loadProjectsFromServer,this.props.pollInterval);},render:function(){return(React.createElement(Project,{data:this.state.data}));}});var Project=React.createClass({displayName:"Project",rawMarkup:function(){var rawMarkup=this.props.data.description_html;return{__html:rawMarkup};},render:function(){var assetNodes=this.props.data.assets.map(function(asset){return(React.createElement(Asset,{key:asset.pk,art:asset.art,project:asset.project,description:asset.description}));});return(React.createElement("div",null,React.createElement("header",null,React.createElement("h2",{className:"lead_head"},this.props.data.client_name)),React.createElement("span",{dangerouslySetInnerHTML:this.rawMarkup()}),React.createElement("ul",{className:"project_asset_list"},assetNodes)));}});var Asset=React.createClass({displayName:"Asset",render:function(){return(React.createElement("li",{className:"asset"},React.createElement("span",{className:"asset_description"},this.props.project,this.props.description),React.createElement("a",{href:this.props.art,"data-title":this.props.project,"data-lightbox":"roadtrip"},React.createElement("img",{src:this.props.art,alt:this.props.description}))))}});ReactDOM.render(React.createElement(ProjectContainer,{url:"/work/api/little-general/",pollInterval:2000}),document.getElementById('project_indiv'));