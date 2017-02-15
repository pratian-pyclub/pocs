f = File.read("/Users/swaathi/Skcript/Pratian/pocs/t.txt")
twi = f.split("\n\n")

channels = []
twi.each do |t|
  list = t.split("\n")
  name = list[0]
  tweets = list[1..-1]
  channels.push({name: name, tweets: tweets})
end

# puts channels
dates = {}
channels.first[:tweets].each do |ch|
  dates[ch.split(" -")[0]] = 0
end

# puts dates
channels.each do |ch|
  ch[:tweets].each do |tw|
    date = tw.split(" -")[0]
    count = tw.split("- ")[1].to_i
    dates[date] += count
  end
end

puts dates
avg_dates = {}
dates.each do |k,v|
  # puts k
  # puts v
  # puts v/9
  avg_dates[k] = v/9
end
puts avg_dates
