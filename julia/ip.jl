using Memento
using JSON
using HTTP
using URIs

# To use included Project.toml to set up environment before running script, uncomment thsese lines
# using Pkg
# Pkg.activate(@__DIR__)
# Pkg.instantiate()

# Set up logging
logger = Memento.config!("info"; fmt="[{date}]: {msg}")
formatter = DefaultFormatter("[{date}]: {msg}"; date_fmt_string="U dd, yyyy HH:MM:SS")

handler = DefaultHandler("gddnsjl.log")
handler.fmt = formatter
push!(logger, handler)

# Function to parse config file
function config()
    path = joinpath(dirname(@__DIR__), "config.json")
    config = JSON.parsefile(path)
    return config
end

function main()
    ip = HTTP.get("https://domains.google.com/checkip").body |> x -> String(x)
    c = config()
    url = URI(parse(URI, "https://$(c["username"]):$(c["password"])@domains.google.com/nic/update"), query = Dict{String, Any}("hostname" => c["hostname"], "myip" => ip))
    rp = HTTP.post(url)
    info(logger, "hostname: $(c["hostname"]) IP: $(ip) response: $(String(rp.body))")
end

main()
