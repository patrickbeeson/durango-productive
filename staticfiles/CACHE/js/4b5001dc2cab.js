var ProjectContainer=React.createClass({displayName:"ProjectContainer",getInitialState:function(){return{data:{assets:[]}};},componentDidMount:function(){$.ajax({url:this.props.url,dataType:'json',cache:false,success:function(data){this.setState({data:data});}.bind(this),error:function(xhr,status,err){console.error(this.props.url,status,err.toString());}.bind(this)});},render:function(){return(React.createElement(Project,{data:this.state.data}));}});var Project=React.createClass({displayName:"Project",render:function(){return(React.createElement("li",{className:"footer_past_projects"},React.createElement("a",{href:"/work/"},React.createElement("img",{src:this.props.data.lead_art,alt:this.props.data.client_name}),"Past Projects")));}});var featuredContainerUrl=$('#project_featured').data('url');ReactDOM.render(React.createElement(ProjectContainer,{url:featuredContainerUrl}),document.getElementById('project_featured'));